from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType, DateType,  DoubleType, StringType
from pyspark.sql.types import StructType, StructField
custom_schema = StructType([
    StructField("part_id", IntegerType(), False),
    StructField("part_name", StringType(), True),
    StructField("manufacturer", StringType(), True),
    StructField("quantity_in_stock", IntegerType(), True),
    StructField("last_restock_date", DateType(), True),
    StructField("next_restock_date", DateType(), True)
])

spark = SparkSession.builder.master("local").appName("BoeingTest").getOrCreate()
df = spark.read.csv("data.csv", header=True, schema=custom_schema)
df.show()
df.printSchema()

(df.write
 .option("header", True)
 .mode("overwrite")
 .csv("data_output.csv"))

# df = spark.read.parquet("path")
# df.show()
# df.write.mode("overwrite").parquet("path+name")
#
# df = spark.read.json("path") #one line
# df = spark.read.option("multiline", "true").json("path")
# df.show()
# df.write.mode("overwrite").json("path+name")
# # repartition onto single file
# df.repartition(1).write.json("path/to/output/single_json_file")