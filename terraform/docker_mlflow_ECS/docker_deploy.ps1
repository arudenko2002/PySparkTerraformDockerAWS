aws ecr create-repository --repository-name mlflow-api --no-cli-pager
# build
docker build -t mlflow-api:latest .

# tag for ECR
docker tag mlflow-api:latest 917819970045.dkr.ecr.us-east-1.amazonaws.com/mlflow-api:latest

# authenticate to ECR (AWS CLI):
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 917819970045.dkr.ecr.us-east-1.amazonaws.com

# push
docker push 917819970045.dkr.ecr.us-east-1.amazonaws.com/mlflow-api:latest