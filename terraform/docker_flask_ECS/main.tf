############################################################
# Provider
############################################################
provider "aws" {
  region = "us-east-1"
}

############################################################
# Networking (VPC + 2 public subnets + IGW + routes)
############################################################
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = { Name = "fargate-vpc" }
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_subnet" "public_a" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
  tags = { Name = "public-a" }
}

resource "aws_subnet" "public_b" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true
  tags = { Name = "public-b" }
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route" "default_inet" {
  route_table_id         = aws_route_table.public_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.igw.id
}

resource "aws_route_table_association" "public_a_assoc" {
  subnet_id      = aws_subnet.public_a.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "public_b_assoc" {
  subnet_id      = aws_subnet.public_b.id
  route_table_id = aws_route_table.public_rt.id
}

############################################################
# Security Groups
############################################################
# ALB accepts HTTP from anywhere
resource "aws_security_group" "alb_sg" {
  name   = "alb-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    description = "HTTP from internet"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "All egress"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = { Name = "alb-sg" }
}

# Tasks only accept traffic from the ALB on port 5000
resource "aws_security_group" "task_sg" {
  name   = "task-sg"
  vpc_id = aws_vpc.main.id

  ingress {
    description     = "From ALB only"
    from_port       = 5000
    to_port         = 5000
    protocol        = "tcp"
    security_groups = [aws_security_group.alb_sg.id]
  }

  egress {
    description = "All egress"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = { Name = "task-sg" }
}

############################################################
# ECS Cluster
############################################################
resource "aws_ecs_cluster" "flask_cluster" {
  name = "flask-cluster"
}

############################################################
# IAM for ECS Task execution (pull image, logs)
############################################################
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = { Service = "ecs-tasks.amazonaws.com" },
      Action    = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_task_exec_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

############################################################
# (Optional) CloudWatch Logs for the container
############################################################
resource "aws_cloudwatch_log_group" "flask_lg" {
  name              = "/ecs/flask"
  retention_in_days = 14
}

############################################################
# ALB + Target Group + Listener
############################################################
resource "aws_lb" "app_alb" {
  name               = "flask-alb"
  load_balancer_type = "application"
  subnets            = [aws_subnet.public_a.id, aws_subnet.public_b.id]
  security_groups    = [aws_security_group.alb_sg.id]
  idle_timeout       = 60

  tags = { Name = "flask-alb" }
}

resource "aws_lb_target_group" "flask_tg" {
  name        = "flask-tg"
  port        = 5000
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = aws_vpc.main.id

  health_check {
    enabled             = true
    path                = "/"
    protocol            = "HTTP"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 5
    matcher             = "200-399"
  }

  tags = { Name = "flask-tg" }
}

resource "aws_lb_listener" "http_80" {
  load_balancer_arn = aws_lb.app_alb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.flask_tg.arn
  }
}

############################################################
# Task Definition (Flask container on port 5000)
############################################################
# resource "aws_ecr_repository" "flask_app" {
#   name = "flask-app"
#
#   image_scanning_configuration {
#     scan_on_push = true
#   }
#
#   tags = {
#     Name = "flask-app"
#   }
# }
resource "aws_ecs_task_definition" "flask_task" {
  family                   = "flask-task"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"
  network_mode             = "awsvpc"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([
    {
      name  = "flask-container"
      image = "917819970045.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest"
      portMappings = [
        {
          containerPort = 5000
          hostPort      = 5000
        }
      ]
      essential = true
      logConfiguration = {
      logDriver = "awslogs"
      options = {
        awslogs-group         = "/ecs/flask"
        awslogs-region        = "us-east-1"
        awslogs-stream-prefix = "flask"
      }
    }
    }
  ])
}

############################################################
# ECS Service wired to the ALB Target Group
############################################################
resource "aws_ecs_service" "flask_service" {
  name            = "flask-service"
  cluster         = aws_ecs_cluster.flask_cluster.id
  task_definition = aws_ecs_task_definition.flask_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = [aws_subnet.public_a.id, aws_subnet.public_b.id]
    assign_public_ip = true
    security_groups  = [aws_security_group.task_sg.id]
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.flask_tg.arn
    container_name   = "flask-container"
    container_port   = 5000
  }

#   deployment_minimum_healthy_percent = 50
#   deployment_maximum_percent         = 200

  depends_on = [aws_lb_listener.http_80]
}

############################################################
# Outputs
############################################################
output "alb_dns_name" {
  value = aws_lb.app_alb.dns_name
}
