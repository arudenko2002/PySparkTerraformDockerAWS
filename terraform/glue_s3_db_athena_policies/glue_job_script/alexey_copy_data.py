import sys
from awsglue.context import GlueContext
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session




# Read from Glue Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="source_database",
    table_name="source_table"
)

datasource.show()

glueContext.write_dynamic_frame.from_options(
    frame=datasource,
    connection_type="s3",
    connection_options={"path": "s3://alexey-athena-dest-bucket/results"},
    format="csv",
    format_options={"withHeader": False}  # 👈 disable header row
)