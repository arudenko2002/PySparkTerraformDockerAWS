"""
Suggestions on fixing Pyspark Streaming
https://www.google.com/search?q=pyspark+terminated+with+error+java.lang.UnsatisfiedLinkError%3A+%27boolean+org.apache.hadoop.io.nativeio.NativeIO%24Windows.access0(java.lang.String%2C+int)%27&rlz=1C1GCEU_enUS1163US1163&oq=pyspark+terminated+with+error+java.lang.UnsatisfiedLinkError%3A+%27boolean+org.apache.hadoop.io.nativeio.NativeIO%24Windows.access0(java.lang.String%2C+int)%27&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDI3ODhqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
"""

from pyspark.sql import SparkSession
import os
from pyspark.sql.functions import col
#install hadoop, add 2 environment variables
os.environ["HADOOP_HOME"] = "C:\\Users\\AlexR\\hadoop\\winutils-master\\winutils-master\\hadoop-3.2.0"
os.environ["hadoop.home.dir"] = "C:\\Users\\AlexR\\hadoop\\winutils-master\\winutils-master\\hadoop-3.2.0\\bin"

def streaming_rate():
    spark = SparkSession.builder.appName("RateSourceExample").getOrCreate()

    df = spark.readStream \
        .format("rate") \
        .option("rowsPerSecond", 10) \
        .load()

    print("AAAAAAAAAA")
    df = df.withColumn("another column", col("value"))

    query = df.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()

# streaming_rate()
"""
-------------------------------------------
Batch: 0
-------------------------------------------
+---------+-----+
|timestamp|value|
+---------+-----+
+---------+-----+

-------------------------------------------
Batch: 1
-------------------------------------------
+--------------------+-----+
|           timestamp|value|
+--------------------+-----+
|2025-06-07 17:24:...|    0|
|2025-06-07 17:24:...|    4|
|2025-06-07 17:24:...|    8|
|2025-06-07 17:24:...|   12|
|2025-06-07 17:24:...|   16|
|2025-06-07 17:24:...|    1|
|2025-06-07 17:24:...|    5|
|2025-06-07 17:24:...|    9|
|2025-06-07 17:24:...|   13|
|2025-06-07 17:24:...|   17|
|2025-06-07 17:24:...|    2|
|2025-06-07 17:24:...|    6|
|2025-06-07 17:24:...|   10|
|2025-06-07 17:24:...|   14|
|2025-06-07 17:24:...|   18|
|2025-06-07 17:24:...|    3|
|2025-06-07 17:24:...|    7|
|2025-06-07 17:24:...|   11|
|2025-06-07 17:24:...|   15|
|2025-06-07 17:24:...|   19|
+--------------------+-----+
...
"""
# First execute socket_tcp_server.py, then streaming.py
def streaming_socket():
    spark = SparkSession.builder.appName("SocketStreamExample").getOrCreate()

    # Read from socket
    lines = spark.readStream \
        .format("socket") \
        .option("host", "localhost") \
        .option("port", 9999) \
        .load()

    # Word count
    from pyspark.sql.functions import explode, split

    words = lines.select(explode(split(lines.value, " ")).alias("word"))
    word_counts = words.groupBy("word").count()
    query = word_counts.writeStream \
        .outputMode("complete") \
        .format("console") \
        .start()
    query.awaitTermination()

# streaming_socket()

"""
-------------------------------------------
Batch: 0
-------------------------------------------
+----+-----+
|word|count|
+----+-----+
+----+-----+

-------------------------------------------
Batch: 1
-------------------------------------------
+-----------+-----+
|       word|count|
+-----------+-----+
|  ggggggggg| 2001|
|  eeeeeeeee| 2001|
|   hhhhhhhh| 2001|
|ddddddddddd| 2001|
|  fffffffff| 2001|
+-----------+-----+

-------------------------------------------
Batch: 2
-------------------------------------------
+-----------+-----+
|       word|count|
+-----------+-----+
|  ggggggggg| 4001|
|  eeeeeeeee| 4001|
|   hhhhhhhh| 4001|
|ddddddddddd| 4001|
|  fffffffff| 4001|
+-----------+-----+

-------------------------------------------
Batch: 3
-------------------------------------------
+-----------+-----+
|       word|count|
+-----------+-----+
|  ggggggggg| 5001|
|  eeeeeeeee| 5001|
|   hhhhhhhh| 5001|
|ddddddddddd| 5001|
|  fffffffff| 5001|
+-----------+-----+

-------------------------------------------
Batch: 4
-------------------------------------------
+-----------+-----+
|       word|count|
+-----------+-----+
|  ggggggggg| 7001|
|  eeeeeeeee| 7001|
|   hhhhhhhh| 7001|
|ddddddddddd| 7001|
|  fffffffff| 7001|
+-----------+-----+

-------------------------------------------
Batch: 5
-------------------------------------------
+-----------+-----+
|       word|count|
+-----------+-----+
|  ggggggggg| 8001|
|  eeeeeeeee| 8001|
|   hhhhhhhh| 8001|
|ddddddddddd| 8001|
|  fffffffff| 8001|
+-----------+-----+

-------------------------------------------
Batch: 6
-------------------------------------------
+-----------+-----+
|       word|count|
+-----------+-----+
|  ggggggggg|10001|
|  eeeeeeeee|10001|
|   hhhhhhhh|10001|
|ddddddddddd|10001|
|  fffffffff|10001|
+-----------+-----+
"""

def streaming_file_csv():
    spark = SparkSession.builder.appName("FileStreamExample").getOrCreate()

    # Read streaming data from a folder
    df = spark.readStream \
        .option("header", "true") \
        .schema("Column1 INT, Column2 STRING, Column3 STRING") \
        .csv("streaming_data_files")

    query = df.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()

#streaming_file_csv()
"""
 Header: Column1,  Column2,  Column3
 Schema: Column1, Column2, Column3
Expected: Column2 but found:  Column2
CSV file: file:///C:/Users/AlexR/PycharmProjects/pythonProject/pyspark/streaming_data_files/data.csv
-------------------------------------------
Batch: 0
-------------------------------------------
+-------+-------+-------+
|Column1|Column2|Column3|
+-------+-------+-------+
|      1|aaaaaaa| bbbbbb|
|      2|aaaaaaa| bbbbbb|
|      3|aaaaaaa| bbbbbb|
|      4|aaaaaaa| bbbbbb|
|      5|aaaaaaa| bbbbbb|
|      6|aaaaaaa| bbbbbb|
|      7|aaaaaaa| bbbbbb|
|      8|aaaaaaa| bbbbbb|
|      9|aaaaaaa| bbbbbb|
|     10|aaaaaaa| bbbbbb|
|     11|aaaaaaa| bbbbbb|
|     12|aaaaaaa| bbbbbb|
|     13|aaaaaaa| bbbbbb|
|     14|aaaaaaa| bbbbbb|
|     15|aaaaaaa| bbbbbb|
|     16|aaaaaaa| bbbbbb|
|     17|aaaaaaa| bbbbbb|
|     18|aaaaaaa| bbbbbb|
|     19|aaaaaaa| bbbbbb|
|     20|aaaaaaa| bbbbbb|
+-------+-------+-------+
only showing top 20 rows
"""

# start consumer,  Then start kafka_producer.py
from kafka import KafkaConsumer
import json

def streaming_kafka():
    consumer = KafkaConsumer(
        'test-topic',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        group_id='my-group'
    )

    print("Listening for messages...")
    for num,message in enumerate(consumer):
        print(f"Received: {num} {message.value}")
        print(message.value["value"])

# streaming_kafka()
"""
Listening for messages...
Received: 0 {'value': 'Hello Kafka 0'}
Hello Kafka 0
Received: 1 {'value': 'Hello Kafka 1'}
Hello Kafka 1
Received: 2 {'value': 'Hello Kafka 2'}
Hello Kafka 2
Received: 3 {'value': 'Hello Kafka 3'}
Hello Kafka 3
Received: 4 {'value': 'Hello Kafka 4'}
Hello Kafka 4
Received: 5 {'value': 'Hello Kafka 5'}
Hello Kafka 5
Received: 6 {'value': 'Hello Kafka 6'}
Hello Kafka 6
Received: 7 {'value': 'Hello Kafka 7'}
Hello Kafka 7
Received: 8 {'value': 'Hello Kafka 8'}
Hello Kafka 8
Received: 9 {'value': 'Hello Kafka 9'}
Hello Kafka 9
Received: 10 {'value': 'Hello Kafka 10'}
Hello Kafka 10
Received: 11 {'value': 'Hello Kafka 11'}
Hello Kafka 11
"""

def streaming_database():
    from pyspark import SparkContext, SparkConf, SQLContext
    appName = "PySpark SQL Server Example - via JDBC"
    master = "local"
    conf = SparkConf().setAppName(appName).setMaster(master).set("spark.driver.extraClassPath",
                                                                 "C:\\Users\\AlexR\\sqljdbc_12.10.1.0_enu\\sqljdbc_12.10\\enu\\jars\\mssql-jdbc-12.10.1.jre8.jar")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    spark = sqlContext.sparkSession

    # Read streaming data from a folder
    df = spark.readStream \
        .option("header", "true") \
        .schema("Column1 INT, Column2 STRING, Column3 STRING") \
        .csv("streaming_data_files")

    def write_database(batch_df, batch_id):
        table = "streaming_output"
        database = "Probe"
        jdbc_url = f"jdbc:sqlserver://localhost:1433;databaseName={database};encrypt=true;trustServerCertificate=true"
        user = "pyspark_user"
        password = "pyspark2025"

        # Write DataFrame to database in append mode
        connection_properties = {
            "user": user,
            "password": password,
            "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
        }
        # Write DataFrame to SQL Server table (append mode)
        batch_df.write.jdbc(
            url=jdbc_url,
            table=table,  # Schema and table name
            mode="append",  # Options: append, overwrite, ignore, error
            properties=connection_properties
        )
        batch_df.show()
    query = df.writeStream \
        .foreachBatch(write_database) \
        .outputMode("update") \
        .start()

    query.awaitTermination()

streaming_database()