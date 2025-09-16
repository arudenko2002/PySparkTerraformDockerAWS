# athena.tf
# resource "aws_athena_workgroup" "athena_wg" {
#   name = "alexey_athena_destination_wg"
#
#   configuration {
#     result_configuration {
#       output_location = "s3://${aws_s3_bucket.athena_dest_bucket.bucket}/results/"
#     }
#   }
# }

# Create S3 bucket for Athena query results
resource "aws_s3_bucket" "athena_query_results" {
  bucket = "alexey-athena-query-results-${random_id.bucket_suffix.hex}"

  # Optional: lifecycle rule to clean up old query results after 30 days
  lifecycle_rule {
    enabled = true
    expiration {
      days = 30
    }
  }
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# Athena workgroup that writes query results into the above bucket
resource "aws_athena_workgroup" "query_results_wg" {
  name = "alexey_athena_query_results_wg"

  configuration {
    enforce_workgroup_configuration = true
    publish_cloudwatch_metrics_enabled = true

    result_configuration {
      output_location = "s3://${aws_s3_bucket.athena_query_results.bucket}/"
      encryption_configuration {
        encryption_option = "SSE_S3"
      }
    }
  }
}


# ====== Glue Database ======
resource "aws_glue_catalog_database" "dest_db" {
  name = "alexey_destination_db"
}

# ====== Option A: Glue Table (manual schema definition) ======
resource "aws_glue_catalog_table" "dest_table" {
  database_name = aws_glue_catalog_database.dest_db.name
  name          = "destination_table"

  table_type = "EXTERNAL_TABLE"

  parameters = {
    classification = "csv"
    has_encrypted_data = "false"
  }

  storage_descriptor {
    location      = "s3://${aws_s3_bucket.athena_dest_bucket.bucket}/results/"
    input_format  = "org.apache.hadoop.mapred.TextInputFormat"
    output_format = "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat"

    ser_de_info {
      name                  = "OpenCSVSerde"
      serialization_library = "org.apache.hadoop.hive.serde2.OpenCSVSerde"

      parameters = {
        "separatorChar" = ","
      }
    }

    columns {
      name = "name"
      type = "string"
    }
    columns {
      name = "title"
      type = "string"
    }
    columns {
      name = "amount"
      type = "int"
    }
  }
}