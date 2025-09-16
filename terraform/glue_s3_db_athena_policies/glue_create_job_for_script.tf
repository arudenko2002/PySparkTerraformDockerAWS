# glue_job.tf
resource "aws_s3_object" "pyspark_script" {
  bucket = aws_s3_bucket.source_bucket.bucket
  key    = "scripts/alexey_copy_data.py"
  source = "glue_job_script/alexey_copy_data.py"
}

resource "aws_glue_job" "copy_job" {
  name     = "alexey_copy_s3_to_athena"
  role_arn = aws_iam_role.glue_role.arn
  command {
    name            = "glueetl"
    python_version  = "3"
    script_location = "s3://${aws_s3_bucket.source_bucket.bucket}/scripts/alexey_copy_data.py"
  }
}

resource "aws_iam_role" "glue_role" {
  name = "glue-job-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { Service = "glue.amazonaws.com" }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "glue_s3_full" {
  role       = aws_iam_role.glue_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}

resource "aws_iam_role_policy_attachment" "glue_athena_full" {
  role       = aws_iam_role.glue_role.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonAthenaFullAccess"
}