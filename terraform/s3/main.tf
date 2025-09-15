provider "aws" {
  region = "ap-southeast-1"
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "example_bucket" {
  bucket = "my-terraform-example-bucket-${random_id.bucket_suffix.hex}"
}
