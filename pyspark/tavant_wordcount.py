from pyspark.sql import SparkSession
import pyspark.sql.functions as functions
from pyspark.sql.functions import col, explode, split, desc

def rdd_word_count():
    spark = SparkSession.builder \
    .master("local") \
    .appName("Word Count") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    text_rdd = spark.read.text("word.txt")
    print("text_rdd=")
    text_rdd.show(truncate=False)
    text_rdd2 = text_rdd.rdd
    print("text_rdd2=",text_rdd2.collect())
    word_rdd = text_rdd2.flatMap(lambda line: line.value.split(' '))
    print("word_rdd=",word_rdd.collect())
    word_map = word_rdd.map(lambda word: (word,1))
    print("word_map=", word_map.collect())
    word_count = word_map.reduceByKey(lambda x,y: x+y)
    print("word_count=",word_count.collect())
    results = word_count.collect()
    for word, count in sorted(results, key=lambda x: x[1], reverse=True):
        print(f"{word}: {count}")

rdd_word_count()

def dataframe_word_count2():
    spark = SparkSession.builder \
        .master("local") \
        .appName("readDataFrame") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    df = spark.read.text("word.txt")
    df2 = df.selectExpr("split(value, ' ') as Words")
    df3 = df2.withColumn("word", explode(col("Words")))
    df4 = df3.groupBy("word").count().orderBy(col("count").desc())
    print("df4=")
    df4.show(truncate=False)
dataframe_word_count2()

def dataframe_word_count3():
    spark = SparkSession.builder \
        .master("local") \
        .appName("readDataFrame") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    df = spark.read.text("word.txt")
    print("df=")
    df.show(truncate=False)
    df3 = df.withColumn("word", explode(split(col("value"), " ")))
    print("df3=")
    df3.show(truncate=False)
    df4 = df3.groupBy("word").count().orderBy(col("count").desc())
    print("df4=")
    df4.show(truncate=False)
dataframe_word_count3()