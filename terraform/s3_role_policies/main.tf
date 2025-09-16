provider "aws" {
  region = "us-east-1"
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "example" {
  bucket = "my-secure-bucket-${random_id.bucket_suffix.hex}"
}

# IAM Role
resource "aws_iam_role" "lambda_role" {
  name = "lambda-execution-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = "sts:AssumeRole",
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# IAM Policy
resource "aws_iam_policy" "lambda_policy" {
  name        = "lambda-access-s3-policy"
  description = "Allow Lambda to access S3 bucket"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Action = [
        "s3:GetObject",
        "s3:PutObject"
      ],
      Effect   = "Allow",
      Resource = "${aws_s3_bucket.example.arn}/*"
    }]
  })
}

# Attach Policy to Role
resource "aws_iam_role_policy_attachment" "lambda_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = aws_iam_policy.lambda_policy.arn
}