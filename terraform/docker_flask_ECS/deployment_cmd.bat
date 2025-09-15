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

terraform apply