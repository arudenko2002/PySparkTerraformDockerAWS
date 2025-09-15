REM create repository for containers
aws ecr create-repository --repository-name flask-app
REM Add permission to user1 create CreateContainerRegistry - AlexeyContainerRegistry  (I added through UI as root)
REM aws iam attach-user-policy --user-name user1 --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryFullAccess
REM user user1 should have permission for the iam:AttachUserPolicy

REM builds the image from local Dockerfile with Docker server running
docker build -t flask-app .

REM tags the image (known to my laptop only so far) for ECR registry
docker tag flask-app:latest 917819970045.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest

REM Authenticate Docker with ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 917819970045.dkr.ecr.us-east-1.amazonaws.com

REM push image to ECR
docker push 917819970045.dkr.ecr.us-east-1.amazonaws.com/flask-app:latest

REM success

@REM Error: repository already exists.  Either run this to move repository (created here from CLI)
@REM under Terraform management
terraform import aws_ecr_repository.flask_app arn:aws:ecr:us-east-1:917819970045:repository/flask-app
@REM or comment out the creation of the new repository, lines 193-203 in main.tf
@REM The again
terraform apply
@REM ...
@REM No changes. Your infrastructure matches the configuration.
@REM
@REM Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
@REM
@REM Apply complete! Resources: 0 added, 0 changed, 0 destroyed.
@REM
@REM Outputs:
@REM
@REM alb_dns_name = "flask-alb-896381247.us-east-1.elb.amazonaws.com"

on Browser:  http://flask-alb-896381247.us-east-1.elb.amazonaws.com
REM "Hello World!"


What we deployed:

1. Networking

VPC – fargate-vpc with CIDR 10.0.0.0/16
Subnets – 2 public subnets:
public-a → 10.0.1.0/24 in us-east-1a
public-b → 10.0.2.0/24 in us-east-1b
Internet Gateway – igw for public internet access
Route Table – public_rt with route 0.0.0.0/0 via IGW
Route Table Associations – each subnet associated with the public route table

2. Security

ALB Security Group (alb-sg) – allows inbound HTTP (80) from anywhere, full outbound
Task Security Group (task-sg) – allows inbound traffic on port 5000 only from the ALB, full outbound

3. ECS (Elastic Container Service)

Cluster – flask-cluster
Task Definition – flask-task
Runs a container flask-container from your ECR repo flask-app
Fargate launch type, CPU 256, Memory 512
Uses ecsTaskExecutionRole IAM role for pulling images and logging
Logs sent to CloudWatch log group /ecs/flask
Service – flask-service
Runs 1 task of flask-task
Attached to an ALB target group
Uses task-sg security group
Runs in both public subnets

4. Application Load Balancer

ALB – flask-alb (internet-facing)
Subnets: public-a, public-b
Security group: alb-sg
Target Group – flask-tg on port 5000
Listener – HTTP port 80 → forwards traffic to flask-tg
DNS Name – flask-alb-1848472230.us-east-1.elb.amazonaws.com (your app endpoint)


EC2:
LoadBalancers
Traget Group
Listeners
Security Groups

VPC:
VPCs
Subnets
Internet Gateways



