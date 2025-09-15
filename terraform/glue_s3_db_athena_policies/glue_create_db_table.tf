# glue.tf
resource "aws_glue_catalog_database" "source_db" {
  name = "source_database"
}

resource "aws_glue_catalog_table" "source_table" {
  name          = "source_table"
  database_name = aws_glue_catalog_database.source_db.name
  table_type    = "EXTERNAL_TABLE"

  storage_descriptor {
    location      = "s3://alexey-source-sample-bucket/data/"
    input_format  = "org.apache.hadoop.mapred.TextInputFormat"
    output_format = "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat"

    ser_de_info {
      name                  = "OpenCSVSerde"
      serialization_library = "org.apache.hadoop.hive.serde2.OpenCSVSerde"
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

    parameters = {
        "skip.header.line.count" = "1"
    }
  }
}