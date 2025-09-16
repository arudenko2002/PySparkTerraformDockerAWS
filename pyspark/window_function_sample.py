from pyspark.sql import SparkSession, Window
from  pyspark.sql.functions import sum
spark = SparkSession.builder.appName("Window").getOrCreate()
df = spark.createDataFrame([
  ["Alice", "2024-01-01", 100],
  ["Alice", "2024-01-02", 200],
  ["Alice", "2024-01-03", 300],
  ["Bob", "2024-01-01", 50],
  ["Bob", "2024-01-02", 100]]
).toDF("name", "date", "amount")
df.show()

windowSpec_running_total = Window.partitionBy("name").orderBy("date")
windowSpec_total = Window.partitionBy("name")
result = df.withColumn("running_total", sum("amount").over(windowSpec_running_total))
result.show()
result2 = result.withColumn("total", sum("amount").over(windowSpec_total))
result2.show()