provider "aws" {
  region = "us-east-1"
}

#Create 2 S3 buckets
resource "aws_s3_bucket" "glue_source_bucket" {
  bucket = "alexey-glue-source-bucket"
}

# resource "aws_s3_bucket" "target_bucket" {
#   bucket = "alexey-target-bucket"
# }

# Upload Glue script to S3
resource "aws_s3_object" "glue_script" {
  bucket = aws_s3_bucket.glue_source_bucket.bucket
  key    = "scripts/s3_etl_script.py"
  source = "${path.module}/glue_job_script/s3_etl_script.py"
}

# IAM Role for Glue
resource "aws_iam_role" "glue_role" {
  name = "glue-loggroup-s3-access-role"

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

resource "aws_iam_role_policy_attachment" "glue_cloudwatch_policy_attachment" {
  role       = aws_iam_role.glue_role.name
  policy_arn = "arn:aws:iam::aws:policy/CloudWatchLogsFullAccess" # Allow writing to CloudWatch Logs
}

resource "aws_cloudwatch_log_group" "custom_glue_log_group" {
  name = "/aws-glue/jobs/alexey-custom-log-group" # Choose a descriptive name for your log group
  retention_in_days = 7 # Adjust retention as needed
}

# Glue Job
resource "aws_glue_job" "alexey_s3_exchange_job" {
  name     = "alexey-glue-s3-cloudwatch-data"
  role_arn = aws_iam_role.glue_role.arn

  command {
    name            = "glueetl"
    script_location = "s3://${aws_s3_bucket.glue_source_bucket.bucket}/${aws_s3_object.glue_script.key}"
    python_version  = "3"
  }

  glue_version = "4.0"

default_arguments = {
  "--job-language"             = "python"
  "--enable-continuous-cloudwatch-log" = "true"
  "--continuous-log-logGroup"  = aws_cloudwatch_log_group.custom_glue_log_group.name
  "--job-bookmark-option"     = "job-bookmark-disable"
  "--custom-logStream-prefix" = "alexey-glue-cloudwatch"
  "--TempDir"                 = "s3://${aws_s3_bucket.glue_source_bucket.bucket}/tmp/"
}
  depends_on = [aws_cloudwatch_log_group.custom_glue_log_group]

  max_capacity = 2
  timeout      = 10
}