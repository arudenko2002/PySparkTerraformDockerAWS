# 1. Create repository (ignore error if it already exists)
try {
    aws ecr create-repository --repository-name flask-app | Out-Null
    Write-Host "Repository 'flask-app' created."
} catch {
    Write-Host "Repository 'flask-app' already exists. Continuing..."
}

# 2. Get AWS Account ID
$ACCOUNT_ID = (aws sts get-caller-identity --query Account --output text)
Write-Host "ACCOUNT_ID = $ACCOUNT_ID"

# 3. Set region
$REGION = "us-east-1"
Write-Host "REGION = $REGION"

# 4. Build ECR URI
$ECR_URI = "$ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/flask-app"
Write-Host "ECR_URI = $ECR_URI"

# 5. Build Docker image
docker build -t flask-app .

# 6. Tag Docker image
docker tag flask-app:latest "${ECR_URI}:latest"

# 7. Authenticate Docker with ECR
aws ecr get-login-password --region $REGION | docker login --username AWS --password-stdin $ECR_URI

# 8. Push Docker image
docker push "${ECR_URI}:latest"