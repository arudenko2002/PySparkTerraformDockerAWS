provider "aws" {
  region = "us-east-1"
}

# Create 2 S3 buckets
resource "aws_s3_bucket" "source_bucket" {
  bucket = "alexey-source-bucket"
}

resource "aws_s3_bucket" "target_bucket" {
  bucket = "alexey-target-bucket"
}

# Upload Glue script to S3
resource "aws_s3_object" "glue_script" {
  bucket = aws_s3_bucket.source_bucket.bucket
  key    = "scripts/s3_etl_script.py"
  source = "${path.module}/glue_job_script/s3_etl_script.py"
}

# IAM Role for Glue
resource "aws_iam_role" "glue_role" {
  name = "glue-s3-access-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Principal = {
        Service = "glue.amazonaws.com"
      }
      Effect = "Allow"
      Sid    = ""
    }]
  })
}

# Attach policies to role
resource "aws_iam_role_policy_attachment" "glue_s3_access" {
  role       = aws_iam_role.glue_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}

resource "aws_iam_role_policy_attachment" "s3_access" {
  role       = aws_iam_role.glue_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}

# Glue Job
resource "aws_glue_job" "alexey_s3_exchange_job" {
  name     = "s3-data-exchange"
  role_arn = aws_iam_role.glue_role.arn

  command {
    name            = "glueetl"
    script_location = "s3://${aws_s3_bucket.source_bucket.bucket}/${aws_s3_object.glue_script.key}"
    python_version  = "3"
  }

  glue_version = "4.0"
  max_capacity = 2
  timeout      = 10
}