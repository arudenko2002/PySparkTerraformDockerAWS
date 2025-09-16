aws ecr delete-repository ^
    --repository-name ollama-api ^
    --region us-east-1 ^
    --force
terraform destroy -auto-approve

