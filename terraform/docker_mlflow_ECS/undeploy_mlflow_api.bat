aws ecr delete-repository ^
    --repository-name mlflow-api ^
    --region us-east-1 ^
    --force
terraform destroy -auto-approve

