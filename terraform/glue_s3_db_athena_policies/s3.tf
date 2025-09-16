# s3.tf
resource "aws_s3_bucket" "source_bucket" {
  bucket = "alexey-source-bucket-input"
}

resource "aws_s3_bucket" "athena_dest_bucket" {
  bucket = "alexey-athena-dest-bucket"
}