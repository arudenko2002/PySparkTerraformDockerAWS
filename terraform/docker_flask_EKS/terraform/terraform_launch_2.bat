# terraform init -upgrade

# to avoid complain that repository already exists:
terraform import aws_ecr_repository.flask_repo flask-app

terraform plan
terraform apply -auto-approve