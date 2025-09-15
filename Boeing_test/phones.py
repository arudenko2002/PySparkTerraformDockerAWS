from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import StringType
from pyspark.sql.functions import regexp_replace,when, col, concat_ws, lit, substring, length, concat

spark = SparkSession.builder.appName("Phones").master("local").getOrCreate()
schema = StructType([
    StructField("Firstame", StringType(), True),
    StructField("Lastname", StringType(), True),
    StructField("Phone", StringType(), True)
])
phone1_df = spark.read.csv("phone1.csv", schema=schema)
phone2_df = spark.read.csv("phone2.csv", schema=schema)

phone = phone1_df.union(phone2_df)
phone.show()

p2 = phone.withColumn("Phone",regexp_replace("Phone","[^0-9]",""))
p2.show()

p3 = p2.withColumn("Phone", when(length(col("Phone")) == 10,
                                    concat(
                                        #str(length(col("Phone"))),
                                        lit("+1("),
                                        substring(col("Phone"),1,3),
                                        lit(") "),
                                        substring(col("Phone"), 4,3),
                                        lit("-"),
                                        substring(col("Phone"), 7,4)
                                    )
                                    ).otherwise(
                                        concat(
                                        #str(length(col("Phone"))),
                                        lit("+"),
                                        substring(col("Phone"), 1, 1),
                                            lit("("),
                                        substring(col("Phone"), 2, 3),
                                        lit(") "),
                                        substring(col("Phone"), 5, 3),
                                        lit("-"),
                                        substring(col("Phone"), 8, 4)
                                        )
                                    ))
p3.show()

p3.repartition(1).write.mode("overwrite").csv("phones_clean")

# df_with_timestamp = df.withColumn("creation_timestamp", current_timestamp())
# df_with_timestamp.show(truncate=False)
#
# logger = logging.getLogger(__name__)
#
# # Initialize SparkSession
# spark = SparkSession.builder.appName("PySparkLoggingExample").getOrCreate()
#
# # Set Spark's log level (optional, but good practice)
# spark.sparkContext.setLogLevel("WARN")
#
# logger.info("Starting PySpark application...")
#
# try:
#     data = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
#     df = spark.createDataFrame(data, ["Name", "Value"])
#
#     logger.debug("DataFrame created successfully.")
#     df.show()
#
#     # Simulate an error
#     # result = 1 / 0
#
# except Exception as e:
#     logger.error(f"An error occurred: {e}", exc_info=True)
#
# df_flattened = df.select(
#     col("id"),
#     col("details.name").alias("name"),
#     col("details.age").alias("age")
# )
#
# df_exploded = df.withColumn("item", explode("items")) \
#                 .select(
#                     col("order_id"),
#                     col("item.item_id").alias("item_id"),
#                     col("item.quantity").alias("quantity")
#                 )
#
# def lambda_handler(event, context):
#     """
#     Handles incoming Lambda events and processes data.
#     Includes error handling for various scenarios.
#     """
#     try:
#         # Simulate processing an event, expecting 'value' in the input
#         data = event.get('data')
#         if not data:
#             raise ValueError("Missing 'data' in the input event.")
#
#         # Simulate a potential error during data processing
#         if 'error_trigger' in data:
#             raise RuntimeError("Simulated processing error.")
#
#         # Perform some operation
#         result = f"Processed: {data.upper()}"
#
#         return {
#             'statusCode': 200,
#             'body': json.dumps({'message': result})
#         }
#
#     except ValueError as e:
#         # Handle specific expected errors (e.g., invalid input)
#         print(f"ValueError: {e}")
#         return {
#             'statusCode': 400,  # Bad Request
#             'body': json.dumps({'error': str(e)})
#         }
#     except RuntimeError as e:
#         # Handle other specific operational errors
#         print(f"RuntimeError: {e}")
#         return {
#             'statusCode': 500,  # Internal Server Error
#             'body': json.dumps({'error': "An internal processing error occurred."})
#         }
#     except Exception as e:
#         # Catch any other unexpected exceptions
#         print(f"Unhandled Exception: {e}")
#         return {
#             'statusCode': 500,
#             'body': json.dumps({'error': "An unexpected error occurred."})
#         }