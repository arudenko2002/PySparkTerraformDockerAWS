import sys
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from awsglue.dynamicframe import DynamicFrame

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Get the GlueLogger
logger = glueContext.get_logger()

# Replace with your source bucket
source_path = "s3://alexey-source-bucket/input/"
target_path = "s3://alexey-target-bucket/output/"

# Load data
df = spark.read.format("csv").option("header", "true").load(source_path)

# Optional: transform logic
df_transformed = df.dropna()



# Emit log messages
logger.info("This is an informational message glue Alexey.")
logger.warn("This is a warning message glue Alexey.")
logger.error("This is an error message glue Alexey.")

# Write to destination
df_transformed.write.mode("overwrite").format("csv").save(target_path)