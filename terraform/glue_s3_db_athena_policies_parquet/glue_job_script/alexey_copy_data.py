import sys
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
import boto3

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# =========================
# CONFIGURATION
# =========================
SOURCE_DATABASE = "source_database"
SOURCE_TABLE = "source_table"
DESTINATION_DATABASE = "alexey_destination_db"
DESTINATION_TABLE = "destination_table"
DESTINATION_PATH = "s3://alexey-athena-dest-bucket/results/"

# 1️⃣ Read from Glue Catalog (source table)
datasource = glueContext.create_dynamic_frame.from_catalog(
    database=SOURCE_DATABASE,
    table_name=SOURCE_TABLE
)

# (Optional) Data type casting to match Athena table schema
# Example: convert string column 'amount' to bigint
datasource = datasource.resolveChoice(specs=[("amount", "cast:long")])

# 2️⃣ Write directly to S3 as Parquet (no headers)
glueContext.write_dynamic_frame.from_options(
    frame=datasource,
    connection_type="s3",
    connection_options={"path": DESTINATION_PATH},
    format="parquet"
)

# 3️⃣ Update Glue Catalog table to point to the new Parquet location
client = boto3.client("glue")

# Get the existing table metadata
table = client.get_table(DatabaseName=DESTINATION_DATABASE, Name=DESTINATION_TABLE)["Table"]

# Update storage descriptor to Parquet
table_input = {
    "Name": DESTINATION_TABLE,
    "StorageDescriptor": {
        "Columns": table["StorageDescriptor"]["Columns"],
        "Location": DESTINATION_PATH,
        "InputFormat": "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat",
        "OutputFormat": "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat",
        "SerdeInfo": {
            "SerializationLibrary": "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"
        }
    }
}

# Send the update request
client.update_table(
    DatabaseName=DESTINATION_DATABASE,
    TableInput=table_input
)

print(f"✅ Data written to {DESTINATION_PATH} as Parquet and Glue Catalog updated.")