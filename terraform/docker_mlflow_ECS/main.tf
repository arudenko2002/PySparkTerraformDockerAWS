provider "aws" {
  region = "us-east-1"
}

# --- Networking ---
resource "aws_vpc" "mlflow_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "mlflow_subnet_a" {
  vpc_id                  = aws_vpc.mlflow_vpc.id
  cidr_block              = "10.0.10.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
}

resource "aws_subnet" "mlflow_subnet_b" {
  vpc_id                  = aws_vpc.mlflow_vpc.id
  cidr_block              = "10.0.11.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true
}

resource "aws_internet_gateway" "mlflow_gw" {
  vpc_id = aws_vpc.mlflow_vpc.id
}

resource "aws_route_table" "mlflow_rt" {
  vpc_id = aws_vpc.mlflow_vpc.id
}

resource "aws_route" "mlflow_internet_access" {
  route_table_id         = aws_route_table.mlflow_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.mlflow_gw.id
}

resource "aws_route_table_association" "mlflow_rta_a" {
  subnet_id      = aws_subnet.mlflow_subnet_a.id
  route_table_id = aws_route_table.mlflow_rt.id
}

resource "aws_route_table_association" "mlflow_rta_b" {
  subnet_id      = aws_subnet.mlflow_subnet_b.id
  route_table_id = aws_route_table.mlflow_rt.id
}

# --- Security Group ---
resource "aws_security_group" "mlflow_alb_sg" {
  vpc_id = aws_vpc.mlflow_vpc.id

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
  # Security Group for ECS tasks
resource "aws_security_group" "mlflow_sg" {
  vpc_id = aws_vpc.mlflow_vpc.id

  ingress {
    from_port       = 8080
    to_port         = 8080
    protocol        = "tcp"
    security_groups = [aws_security_group.mlflow_alb_sg.id]  # ALB can reach ECS
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# --- ECS Cluster ---
resource "aws_ecs_cluster" "mlflow_cluster" {
  name = "mlflow-cluster"
}

# --- IAM Role for Task Execution ---
resource "aws_iam_role" "ecs_task_execution_role" {
  name = "ecsTaskExecutionRole"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "ecs-tasks.amazonaws.com"
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ecs_task_execution_role_policy" {
  role       = aws_iam_role.ecs_task_execution_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

# --- CloudWatch Log Group ---
resource "aws_cloudwatch_log_group" "mlflow_logs" {
  name              = "/ecs/mlflow-api"
  retention_in_days = 7
}

# --- Task Definition ---
resource "aws_ecs_task_definition" "mlflow_task" {
  family                   = "mlflow-api"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = "512"
  memory                   = "1024"
  execution_role_arn       = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([
    {
      name      = "mlflow-api"
      image     = "917819970045.dkr.ecr.us-east-1.amazonaws.com/mlflow-api:latest"
      essential = true
      portMappings = [{
        containerPort = 8080
        hostPort      = 8080
        protocol      = "tcp"
      }]
      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = aws_cloudwatch_log_group.mlflow_logs.name
          awslogs-region        = "us-east-1"
          awslogs-stream-prefix = "ecs"
        }
      }
    }
  ])
}

# --- ALB ---
resource "aws_lb" "mlflow_alb" {
  name               = "mlflow-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.mlflow_alb_sg.id]
  subnets            = [
    aws_subnet.mlflow_subnet_a.id,
    aws_subnet.mlflow_subnet_b.id
  ]
}

resource "aws_lb_target_group" "mlflow_tg" {
  name        = "mlflow-tg"
  port        = 8080
  protocol    = "HTTP"
  vpc_id      = aws_vpc.mlflow_vpc.id
  target_type = "ip"

  health_check {
    path                = "/predict"
    interval            = 30
    timeout             = 5
    healthy_threshold   = 2
    unhealthy_threshold = 2
    matcher             = "200-399"
  }
}

resource "aws_lb_listener" "mlflow_listener" {
  load_balancer_arn = aws_lb.mlflow_alb.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.mlflow_tg.arn
  }
}

# --- ECS Service ---
resource "aws_ecs_service" "mlflow_service" {
  name            = "mlflow-service"
  cluster         = aws_ecs_cluster.mlflow_cluster.id
  task_definition = aws_ecs_task_definition.mlflow_task.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [
      aws_subnet.mlflow_subnet_a.id,
      aws_subnet.mlflow_subnet_b.id
    ]
    assign_public_ip = true
    security_groups  = [aws_security_group.mlflow_sg.id]
  }

  load_balancer {
    target_group_arn = aws_lb_target_group.mlflow_tg.arn
    container_name   = "mlflow-api"
    container_port   = 8080
  }

  depends_on = [aws_lb_listener.mlflow_listener]
}