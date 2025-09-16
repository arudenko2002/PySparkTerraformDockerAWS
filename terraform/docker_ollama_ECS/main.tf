provider "aws" {
  region = "us-east-1"
}

############################
# VPC
############################
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
}

resource "aws_subnet" "public_a" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
}

resource "aws_subnet" "public_b" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
}

resource "aws_route_table_association" "public_a" {
  subnet_id      = aws_subnet.public_a.id
  route_table_id = aws_route_table.public.id
}

resource "aws_route_table_association" "public_b" {
  subnet_id      = aws_subnet.public_b.id
  route_table_id = aws_route_table.public.id
}

############################
# Security Groups
############################
resource "aws_security_group" "alb_sg" {
  name        = "ollama-alb-sg"
  description = "Allow HTTP traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "ecs_sg" {
  name        = "ollama-ecs-sg"
  description = "Allow container ports"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port       = 8080
    to_port         = 8080
    protocol        = "tcp"
    security_groups = [aws_security_group.alb_sg.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

############################
# CloudWatch Log Group
############################
resource "aws_cloudwatch_log_group" "ollama" {
  name              = "/ecs/ollama"
  retention_in_days = 7
}

############################
# ECS Cluster
############################
resource "aws_ecs_cluster" "ollama" {
  name = "ollama-cluster"
}

############################
# ECS Task Definition
############################
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action    = "sts:AssumeRole"
      Effect    = "Allow"
      Principal = { Service = "ecs-tasks.amazonaws.com" }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_attach" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_ecs_task_definition" "ollama_task" {
  family                   = "ollama-api"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "4096"
  memory                   = "16384"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn
  task_role_arn            = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([{
    name      = "ollama-api"
    image     = "917819970045.dkr.ecr.us-east-1.amazonaws.com/ollama-api:latest"
    essential = true
    portMappings = [
      { containerPort = 8080, hostPort = 8080, protocol = "tcp" }
    ]
    environment = [
      { name = "OLLAMA_HOST", value = "http://127.0.0.1:11434" }
    ]
    logConfiguration = {
      logDriver = "awslogs"
      options = {
        "awslogs-group"         = "/ecs/ollama"
        "awslogs-region"        = "us-east-1"
        "awslogs-stream-prefix" = "ollama"
      }
    }
  }])
}

############################
# ALB
############################
resource "aws_lb" "ollama_alb" {
  name               = "ollama-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb_sg.id]
  subnets            = [aws_subnet.public_a.id, aws_subnet.public_b.id]
  idle_timeout = 3600
}

resource "aws_lb_target_group" "ollama_tg" {
  name        = "ollama-tg"
  port        = 8080
  protocol    = "HTTP"
  vpc_id      = aws_vpc.main.id
  target_type = "ip"
  health_check {
    path                = "/"
    port                = "8080"
    healthy_threshold   = 2
    unhealthy_threshold = 2
    interval            = 10
    matcher             = "200"
    timeout             = 9
  }
}

resource "aws_lb_listener" "ollama_listener" {
  load_balancer_arn = aws_lb.ollama_alb.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.ollama_tg.arn
  }
}

############################
# ECS Service
############################
resource "aws_ecs_service" "ollama_service" {
  name            = "ollama-service"
  cluster         = aws_ecs_cluster.ollama.id
  task_definition = aws_ecs_task_definition.ollama_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets         = [aws_subnet.public_a.id, aws_subnet.public_b.id]
    security_groups = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.ollama_tg.arn
    container_name   = "ollama-api"
    container_port   = 8080
  }

  depends_on = [aws_lb_listener.ollama_listener]
}
