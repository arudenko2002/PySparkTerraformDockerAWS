provider "aws" {
  region = "us-east-1"
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "lambda_bucket" {
  bucket = "my-lambda-code-bucket-${random_id.bucket_suffix.hex}"
}

# 1. Create an S3 bucket (optional, used in Lambda)
# resource "aws_s3_bucket" "lambda_bucket" {
#   bucket = "my-lambda-code-bucket-2025"
# }

# 2. IAM Role for Lambda
resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda-exec-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = {
        Service = "lambda.amazonaws.com"
      },
      Action = "sts:AssumeRole"
    }]
  })
}

# 3. IAM Policy: Allow Lambda to access S3 and write to logs
resource "aws_iam_policy" "lambda_policy" {
  name = "lambda-s3-access-policy"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ],
        Resource = "arn:aws:s3:::my-lambda-code-bucket-2025/*"
      },
      {
        Effect = "Allow",
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        Resource = "*"
      }
    ]
  })
}

# 4. Attach policy to role
resource "aws_iam_role_policy_attachment" "attach" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = aws_iam_policy.lambda_policy.arn
}

# 5. Archive Lambda code
data "archive_file" "lambda_zip" {
  type        = "zip"
  source_file = "${path.module}/lambda/lambda_function.py"
  output_path = "${path.module}/lambda_function.zip"
}

# 6. Upload zip to S3 (or you can use local zip)
resource "aws_s3_object" "lambda_object" {
  bucket = aws_s3_bucket.lambda_bucket.id
  key    = "lambda_function.zip"
  source = data.archive_file.lambda_zip.output_path
}

# 6.6 cloudwatch_log_group
resource "aws_cloudwatch_log_group" "custom_lambda_log_group" {
  name              = "/aws/lambda/my-custom-lambda-logs" # Name your log group
  retention_in_days = 1                                 # Set desired retention days

  tags = {
    Environment = "production"
    Application = "my-application"
  }
}

# 7. Lambda function
resource "aws_lambda_function" "alexey_lambda_function" {
  function_name = "my_lambda_function"
  role          = aws_iam_role.lambda_exec_role.arn
  handler       = "lambda_function.handler"
  runtime       = "python3.9"

  s3_bucket = aws_s3_bucket.lambda_bucket.id
  s3_key    = aws_s3_object.lambda_object.key

  # Configure logging for the Lambda function
  logging_config {
    application_log_level = "INFO" # Set the desired application log level (e.g., INFO, WARN, ERROR)
    log_format            = "JSON" # Choose log format (Text or JSON)
    log_group             = aws_cloudwatch_log_group.custom_lambda_log_group.name # Specify the custom log group
  }
}