from pyspark.sql import SparkSession #Main entry point for DataFrame and SQL functionality.
from pyspark.sql.functions import col, coalesce, sum as _sum, desc, udf
from pyspark.sql import functions as func
# import window module
from pyspark.sql import Window

def join_df_coalesce2():
    spark = SparkSession.builder \
    .master("local") \
    .appName("Disney Test") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    df1 = spark.createDataFrame([(1, "Old_name1",111),(2,"Old_name2",222),(3,"Old_name3", 333),(4,"Old_name4",444)], ('AM_ID', 'Name',"Clicks"))
    df2 = spark.createDataFrame([(2, "New_name2"),(3,"New_name3")], ('AM_ID', 'Name'))
    df1_2 = df1.select(*(col(x).alias(x + '_df1') for x in df1.columns))
    df2_2 = df2.select(*(col(x).alias(x + '_df2') for x in df2.columns))
    print("df1=")
    df1.show()
    print("df1_2=")
    df1_2.show()
    print("df2=")
    df2.show()
    print("df2_2=")
    df2_2.show()
    df3 = df1_2.join(df2_2, col('AM_ID_df1')==col('AM_ID_df2'), "left")
    print("df3=")
    df3.show()
    df4 = df3.withColumn("Name", coalesce(col("Name_df2"),col("Name_df1")))
    print("df4=")
    df4.show()
    df5 = df4.select(col("AM_ID_df1").alias("AM_ID"), col("Name"), col("Clicks_df1").alias("Clicks"))
    print("df5=")
    df5.show()
    spark.stop()
# join_df_coalesce()
"""
df1=
+-----+---------+------+
|AM_ID|     Name|Clicks|
+-----+---------+------+
|    1|Old_name1|   111|
|    2|Old_name2|   222|
|    3|Old_name3|   333|
|    4|Old_name4|   444|
+-----+---------+------+

df1_2=
+---------+---------+----------+
|AM_ID_df1| Name_df1|Clicks_df1|
+---------+---------+----------+
|        1|Old_name1|       111|
|        2|Old_name2|       222|
|        3|Old_name3|       333|
|        4|Old_name4|       444|
+---------+---------+----------+

df2=
+-----+---------+
|AM_ID|     Name|
+-----+---------+
|    2|New_name2|
|    3|New_name3|
+-----+---------+

df2_2=
+---------+---------+
|AM_ID_df2| Name_df2|
+---------+---------+
|        2|New_name2|
|        3|New_name3|
+---------+---------+

df3=
+---------+---------+----------+---------+---------+
|AM_ID_df1| Name_df1|Clicks_df1|AM_ID_df2| Name_df2|
+---------+---------+----------+---------+---------+
|        1|Old_name1|       111|     NULL|     NULL|
|        3|Old_name3|       333|        3|New_name3|
|        2|Old_name2|       222|        2|New_name2|
|        4|Old_name4|       444|     NULL|     NULL|
+---------+---------+----------+---------+---------+

df4=
25/05/17 15:30:15 WARN GarbageCollectionMetrics: To enable non-built-in garbage collector(s) List(G1 Concurrent GC), users should configure it(them) to spark.eventLog.gcMetrics.youngGenerationGarbageCollectors or spark.eventLog.gcMetrics.oldGenerationGarbageCollectors
+---------+---------+----------+---------+---------+---------+
|AM_ID_df1| Name_df1|Clicks_df1|AM_ID_df2| Name_df2|     Name|
+---------+---------+----------+---------+---------+---------+
|        1|Old_name1|       111|     NULL|     NULL|Old_name1|
|        3|Old_name3|       333|        3|New_name3|New_name3|
|        2|Old_name2|       222|        2|New_name2|New_name2|
|        4|Old_name4|       444|     NULL|     NULL|Old_name4|
+---------+---------+----------+---------+---------+---------+

df5=
+-----+---------+------+
|AM_ID|     Name|Clicks|
+-----+---------+------+
|    1|Old_name1|   111|
|    3|New_name3|   333|
|    2|New_name2|   222|
|    4|Old_name4|   444|
+-----+---------+------+
"""
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
def join_df_coalesce3():
    spark = SparkSession.builder \
    .master("local") \
    .appName("Disney Test") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

    schema1 = StructType([
        StructField("AM_ID", IntegerType(), True),
        StructField("Name", StringType(), True),
        StructField("Clicks", IntegerType(), True)])
    df1 = spark.read.csv("disney_file1.csv", schema=schema1)
    print("df1=")
    df1.show()

    schema2 = StructType([
        StructField("AM_ID", IntegerType(), True),
        StructField("Name", StringType(), True)])
    df2 = spark.read.csv("disney_file2.csv", schema=schema2)
    print("df2=")
    df2.show()

    df1_2 = df1.select(col("AM_ID"), col("Name").alias("Name_df1"), col("Clicks"))
    print("df1_2=")
    df1_2.show()

    df2_2 = df2.select(col("AM_ID"), col("Name").alias("Name_df2"))
    print("df2_2=")
    df2_2.show()
    df3 = df1_2.join(df2_2, "AM_ID", "left")
    print("df3=")
    df3.show()
    df4 = df3.withColumn("Name", coalesce(col("Name_df2"), col("Name_df1")))
    print("df4=")
    df4.show()
    df4_2 = df4.withColumn("Name", col("Clicks"))
    print("df4_2")
    df4_2.show()
    df5 = df4.select(col("AM_ID"),col("Name"), col("Clicks"))
    print("df5=")
    df5.show()

def join_df_coalesce():
    spark = SparkSession.builder \
    .master("local") \
    .appName("Disney Test") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

    schema1 = StructType([
        StructField("AM_ID", IntegerType(), True),
        StructField("Name", StringType(), True),
        StructField("Clicks", IntegerType(), True)])
    df1 = spark.read.csv("disney_file1.csv", schema=schema1)
    print("df1=")
    df1.show()

    schema2 = StructType([
        StructField("AM_ID", IntegerType(), True),
        StructField("Name", StringType(), True)])
    df2 = spark.read.csv("disney_file2.csv", schema=schema2)
    print("df2=")
    df2.show()

    df2_2 = df2.withColumnRenamed("Name","Name_df2")

    rename_AM_ID = False  # Either rename AM_ID field and join with both AM_ID columns, or not, only one AM_ID column stays
    if rename_AM_ID:
        df2_2 = df2_2.withColumnRenamed("AM_ID","AM_ID_df2")
        print("df2_2=")
        df2_2.show()
        df3 = df1.join(df2_2, [df1.AM_ID == df2_2.AM_ID_df2], "left")
        print("df33=")
        df3.show()
    else:
        df3 = df1.join(df2_2, "AM_ID", "left")
        print("df31=")
        df3.show()
        df3 = df1.join(df2_2, ["AM_ID"], "left")
        print("df32=")
        df3.show()

    df4 = df3.withColumn("Name", coalesce("Name_df2", "Name"))
    print("df4=")
    df4.show()

    df5 = df4.drop("Name_df2").drop("AM_ID_df2")
    print("df5=")
    df5.show()

#join_df_coalesce()

"""
df1=
+-----+----------+------+
|AM_ID|      Name|Clicks|
+-----+----------+------+
|    1| Old_name1|   111|
|    2| Old_name2|   222|
|    3| Old_name3|   333|
|    4| Old_name4|   444|
+-----+----------+------+

df2=
+-----+----------+
|AM_ID|      Name|
+-----+----------+
|    2| New_name2|
|    3| New_name3|
+-----+----------+

df31=
+-----+----------+------+----------+
|AM_ID|      Name|Clicks|  Name_df2|
+-----+----------+------+----------+
|    1| Old_name1|   111|      NULL|
|    2| Old_name2|   222| New_name2|
|    3| Old_name3|   333| New_name3|
|    4| Old_name4|   444|      NULL|
+-----+----------+------+----------+

df32=
+-----+----------+------+----------+
|AM_ID|      Name|Clicks|  Name_df2|
+-----+----------+------+----------+
|    1| Old_name1|   111|      NULL|
|    2| Old_name2|   222| New_name2|
|    3| Old_name3|   333| New_name3|
|    4| Old_name4|   444|      NULL|
+-----+----------+------+----------+

df4=
+-----+----------+------+----------+
|AM_ID|      Name|Clicks|  Name_df2|
+-----+----------+------+----------+
|    1| Old_name1|   111|      NULL|
|    2| New_name2|   222| New_name2|
|    3| New_name3|   333| New_name3|
|    4| Old_name4|   444|      NULL|
+-----+----------+------+----------+

df5=
+-----+----------+------+
|AM_ID|      Name|Clicks|
+-----+----------+------+
|    1| Old_name1|   111|
|    2| New_name2|   222|
|    3| New_name3|   333|
|    4| Old_name4|   444|
+-----+----------+------+
"""

# Group by exercise
def group_by_exercise():
    spark =  SparkSession.builder.master("local").appName("Disney Test").config("spark.some.config.option", "some-value").getOrCreate()
    data = [["A",1],["B",2],["C",3],["A",9],["B",8],["C",7]]
    columns = ["KEY","VALUE"]
    df1 = spark.createDataFrame(data,columns)
    print("df1=")
    df1.show()

    df_count = df1.groupby(["KEY"]).count()
    print("1 df_count=")
    df_count.show()

    df_sum = df1.groupby("KEY").sum("VALUE")
    print("2 df_sum=")
    df_sum.show()
    # Rename column with sum(VALUE) to sum_values
    df_sum2 = df_sum.withColumnRenamed("sum(VALUE)","sum_values")
    print("3 df_sum2=")
    df_sum2.show()

    # with AGG function, _sum is spark sum working on column as opposed to in-built sum that adds iterables, e.g.array
    df_agg_sum2 = df1.groupby("KEY").agg(_sum("VALUE").alias('summa_by_key'), func.count("KEY").alias("count_by_key"))
    print("4 df_agg_sum2=")
    df_agg_sum2.show()

    # with Window function
    df_sum_Window = df1.withColumn("sum_by_key_Window", func.sum("VALUE").over(Window.partitionBy("KEY")))
    print(" 5 df_sum_Window=")
    df_sum_Window.show()

    # with Window function with over(Window.orderBy()) with empty orderBy() makes total cover the entire table,
    # otherwise it treats the function call as if partitionBy("KEY") is used
    df_sum_Window = df1.withColumn("sum_by_key_Window", func.sum("VALUE").over(Window.orderBy()))
    print(" 5.5 df_sum_Window=")
    df_sum_Window.show()

    # with Window function
    df_count_Window = df1.withColumn("count_by_key_Window", func.count("VALUE").over(Window.partitionBy("KEY")))
    print("6 df_count_Window=")
    df_count_Window.show()

    # with Window function with over(Window.orderBy()) with empty orderBy() makes total cover the entire table,
    # otherwise it treats the function call as if partitionBy("KEY") is used
    df_count_Window = df1.withColumn("count_by_key_Window", func.count("VALUE").over(Window.orderBy()))
    print("6.5 df_count_Window=")
    df_count_Window.show()

    # with Window function
    df_row_number = df1.withColumn("row_number_by_key_Window", func.row_number().over(Window.partitionBy("KEY").orderBy("KEY")))
    print("7 ROW COUNT df_row_number=")
    df_row_number.show()

    # with Window function with over(Window.orderBy()) with empty orderBy() makes total cover the entire table,
    # otherwise it treats the function call as if partitionBy("KEY") is used
    df_row_number = df1.withColumn("row_number_by_key_Window", func.row_number().over(Window.orderBy("KEY")))
    print("7.5 ROW COUNT df_row_number=")
    df_row_number.show()

    df_row_number2 = df_row_number.filter(df_row_number.row_number_by_key_Window == 2)
    print("8 Filter ROW COUNT df_row_number2=")
    df_row_number2.show()

    # with Window function
    df_row_number3 = df1.withColumn("row_number_by_key_Window", func.row_number().over(Window.orderBy(["KEY", "VALUE"])))
    print("9 Order By KEY, VALUE df_row_number3=")
    df_row_number3.show()

    # with Window function
    df_row_number4 = df1.withColumn("sum_by_key_Window", func.row_number().over(Window.orderBy(["KEY", desc("VALUE")])))
    print("10 Order By KEY, VALUE DESC df_row_number3=")
    df_row_number4.show()

    def polynomial(x):
        return x*x + x + 1

    udf_polynomial = udf(polynomial, returnType=IntegerType())
    df_row_udf = df_row_number4.withColumn("udf_polynomial x*x+x+1", udf_polynomial(col("sum_by_key_Window")))
    print("11 udf function applied =")
    df_row_udf.show()


group_by_exercise()
"""
df1=
+---+-----+
|KEY|VALUE|
+---+-----+
|  A|    1|
|  B|    2|
|  C|    3|
|  A|    9|
|  B|    8|
|  C|    7|
+---+-----+

df_count=
+---+-----+
|KEY|count|
+---+-----+
|  B|    2|
|  C|    2|
|  A|    2|
+---+-----+

df_sum=
+---+----------+
|KEY|sum(VALUE)|
+---+----------+
|  B|        10|
|  C|        10|
|  A|        10|
+---+----------+

+---+----------+
|KEY|sum_values|
+---+----------+
|  B|        10|
|  C|        10|
|  A|        10|
+---+----------+

df_agg_sum2=
+---+------------+------------+
|KEY|summa_by_key|count_by_key|
+---+------------+------------+
|  B|          10|           2|
|  C|          10|           2|
|  A|          10|           2|
+---+------------+------------+

df_sum_Window=
+---+-----+-----------------+
|KEY|VALUE|sum_by_key_Window|
+---+-----+-----------------+
|  A|    1|               10|
|  A|    9|               10|
|  B|    2|               10|
|  B|    8|               10|
|  C|    3|               10|
|  C|    7|               10|
+---+-----+-----------------+

df_count_Window=
+---+-----+-----------------+
|KEY|VALUE|sum_by_key_Window|
+---+-----+-----------------+
|  A|    1|                2|
|  A|    9|                2|
|  B|    2|                2|
|  B|    8|                2|
|  C|    3|                2|
|  C|    7|                2|
+---+-----+-----------------+

ROW COUNT df_row_number=
+---+-----+-----------------+
|KEY|VALUE|sum_by_key_Window|
+---+-----+-----------------+
|  A|    1|                1|
|  A|    9|                2|
|  B|    2|                1|
|  B|    8|                2|
|  C|    3|                1|
|  C|    7|                2|
+---+-----+-----------------+

ROW COUNT df_row_number2=
+---+-----+-----------------+
|KEY|VALUE|sum_by_key_Window|
+---+-----+-----------------+
|  A|    9|                2|
|  B|    8|                2|
|  C|    7|                2|
+---+-----+-----------------+

Order By KEY, VALUE df_row_number3=
+---+-----+-----------------+
|KEY|VALUE|sum_by_key_Window|
+---+-----+-----------------+
|  A|    1|                1|
|  A|    9|                2|
|  B|    2|                3|
|  B|    8|                4|
|  C|    3|                5|
|  C|    7|                6|
+---+-----+-----------------+

Order By KEY, VALUE DESC df_row_number3=
+---+-----+-----------------+
|KEY|VALUE|sum_by_key_Window|
+---+-----+-----------------+
|  A|    9|                1|
|  A|    1|                2|
|  B|    8|                3|
|  B|    2|                4|
|  C|    7|                5|
|  C|    3|                6|
+---+-----+-----------------+
"""

def pysql_coalesce():
    array1 = [[1, "Old Name1", 1], [2, "Old Name2", 2], [3, "Old Name3", 3], [4, "Old Name4", 4],
              [1, "Old Name1", 1], [2, "Old Name2", 2], [3, "Old Name3", 3], [4, "Old Name4", 4]]
    array2 = [[2, "New Name2"], [3, "New Name3"]]
    # Create SparkSession
    spark = SparkSession.builder.master("local").appName("Practice").getOrCreate()
    # Create DF
    df1 = spark.createDataFrame(array1, ["ID", "Name", "Score"])
    df2 = spark.createDataFrame(array2, ["ID", "Name"])
    print("df1=")
    df1.show()
    print("df2=")
    df2.show()
    df1.createOrReplaceTempView("df1_table")
    df2.createOrReplaceTempView("df2_table")
    sql = """
        SELECT df1_table.ID, coalesce(df2_table.Name, df1_table.Name) as Name, score 
        from df1_table 
        left join df2_table 
        on df1_table.ID=df2_table.ID
        order by ID
    """
    df3 = spark.sql(sql)
    print("df3=")
    df3.show()
    sql2 = """
        SELECT df1_table.ID, coalesce(df2_table.Name, df1_table.Name) as Name, count(df1_table.ID) as Count, sum(score) as Score
        from df1_table               
        left join df2_table   
        on df1_table.ID=df2_table.ID
        Group by   df1_table.ID, coalesce(df2_table.Name, df1_table.Name)
        Order by ID
    """
    df4 = spark.sql(sql2)
    print("df4=")
    df4.show()

    df2_2 = df2.select("ID", col("Name").alias("Name_df2"))
    df5 = df1.join(func.broadcast(df2_2), "ID", "left")
    print("broadcast df5=")
    df5.show()

    df6 = df5.withColumn("Name", coalesce("Name_df2", "Name")).select("ID","Name", "Score").orderBy("ID")
    print("df6=")
    df6.show()

    df7 = df6.groupBy("ID", "Name").agg(func.count("ID").alias("Count"), func.sum("Score").alias("Score")).orderBy("ID")
    print("df7=")
    df7.show()

# pysql_coalesce()

"""
df1=
+---+---------+-----+
| ID|     Name|Score|
+---+---------+-----+
|  1|Old Name1|    1|
|  2|Old Name2|    2|
|  3|Old Name3|    3|
|  4|Old Name4|    4|
|  1|Old Name1|    1|
|  2|Old Name2|    2|
|  3|Old Name3|    3|
|  4|Old Name4|    4|
+---+---------+-----+

df2=
25/05/23 17:46:38 WARN GarbageCollectionMetrics: To enable non-built-in garbage collector(s) List(G1 Concurrent GC), users should configure it(them) to spark.eventLog.gcMetrics.youngGenerationGarbageCollectors or spark.eventLog.gcMetrics.oldGenerationGarbageCollectors
+---+---------+
| ID|     Name|
+---+---------+
|  2|New Name2|
|  3|New Name3|
+---+---------+

df3=
+---+---------+-----+
| ID|     Name|score|
+---+---------+-----+
|  1|Old Name1|    1|
|  1|Old Name1|    1|
|  2|New Name2|    2|
|  2|New Name2|    2|
|  3|New Name3|    3|
|  3|New Name3|    3|
|  4|Old Name4|    4|
|  4|Old Name4|    4|
+---+---------+-----+

df4=
+---+---------+-----+-----+
| ID|     Name|Count|Score|
+---+---------+-----+-----+
|  1|Old Name1|    2|    2|
|  2|New Name2|    2|    4|
|  3|New Name3|    2|    6|
|  4|Old Name4|    2|    8|
+---+---------+-----+-----+

broadcast df5=
+---+---------+-----+---------+
| ID|     Name|Score| Name_df2|
+---+---------+-----+---------+
|  1|Old Name1|    1|     NULL|
|  2|Old Name2|    2|New Name2|
|  3|Old Name3|    3|New Name3|
|  4|Old Name4|    4|     NULL|
|  1|Old Name1|    1|     NULL|
|  2|Old Name2|    2|New Name2|
|  3|Old Name3|    3|New Name3|
|  4|Old Name4|    4|     NULL|
+---+---------+-----+---------+

df6=
+---+---------+-----+
| ID|     Name|Score|
+---+---------+-----+
|  1|Old Name1|    1|
|  1|Old Name1|    1|
|  2|New Name2|    2|
|  2|New Name2|    2|
|  3|New Name3|    3|
|  3|New Name3|    3|
|  4|Old Name4|    4|
|  4|Old Name4|    4|
+---+---------+-----+

df7=
+---+---------+-----+-----+
| ID|     Name|Count|Score|
+---+---------+-----+-----+
|  1|Old Name1|    2|    2|
|  2|New Name2|    2|    4|
|  3|New Name3|    2|    6|
|  4|Old Name4|    2|    8|
+---+---------+-----+-----+
"""


def Redshift():
    from pyspark.sql import SQLContext
    from pyspark.conf import SparkConf
    from pyspark.sql import SparkSession
    config = SparkConf().setAppName("Redshift")
    sc = SparkContext(conf=config)
    sql_context = SQLContext(sc)

    # Read data frame(?) from a table
    df = sql_context.read \
        .format("com.databricks.spark.redshift") \
        .option("url", "jdbc:redshift://redshifthost:5439/database?user=username&password=pass") \
        .option("dbtable", "my_table") \
        .option("tempdir", "s3n://path/for/temp/data") \
        .load()

    # Read data from a query
    df = sql_context.read \
        .format("com.databricks.spark.redshift") \
        .option("url", "jdbc:redshift://redshifthost:5439/database?user=username&password=pass") \
        .option("query", "select x, count(*) my_table group by x") \
        .option("tempdir", "s3n://path/for/temp/data") \
        .load()

    # Write back to a table
    df.write \
        .format("com.databricks.spark.redshift") \
        .option("url", "jdbc:redshift://redshifthost:5439/database?user=username&password=pass") \
        .option("dbtable", "my_table_copy") \
        .option("tempdir", "s3n://path/for/temp/data") \
        .mode("error") \
        .save()

    # Using IAM Role based authentication
    df.write \
        .format("com.databricks.spark.redshift") \
        .option("url", "jdbc:redshift://redshifthost:5439/database?user=username&password=pass") \
        .option("dbtable", "my_table_copy") \
        .option("tempdir", "s3n://path/for/temp/data") \
        .option("aws_iam_role", "arn:aws:iam::123456789000:role/redshift_iam_role") \
        .mode("error") \
        .save()

    # initialize the spark session
    spark = SparkSession.builder.master("yarn").appName("Connect to redshift").enableHiveSupport().getOrCreate()
    sc = spark.sparkContext
    sqlContext = HiveContext(sc)

    sc._jsc.hadoopConfiguration().set("fs.s3.awsAccessKeyId", "<ACCESSKEYID>")
    sc._jsc.hadoopConfiguration().set("fs.s3.awsSecretAccessKey", "<ACCESSKEYSECTRET>")

    taxonomyDf = sqlContext.read \
        .format("com.databricks.spark.redshift") \
        .option("url", "jdbc:postgresql://url.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") \
        .option("dbtable", "table_name") \
        .option("tempdir", "s3://mybucket/") \
        .load()


def copyRedshift():
    # postgres driver needed
    import psycopg2
    # Amazon Redshift connect string
    conn_string = "dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"
    # connect to Redshift (database should be open to the world)
    con = psycopg2.connect(conn_string);

    # fiction variaBLES
    to_table = ""
    filename = ""
    delim = ""
    quote = ""
    gzip = ""
    AWS_ACCESS_KEY_ID = ""
    AWS_SECRET_ACCESS_KEY = ""
    # end of fiction variables
    sql = """COPY %s FROM '%s' credentials 'aws_access_key_id=%s; aws_secret_access_key=%s' delimiter '%s' FORMAT CSV %s %s; commit;""" % (
    to_table, filename, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, delim, quote, gzip)

    # Here
    #  fn - s3://path_to__input_file.gz
    #  gzip = 'gzip'

    cur = con.cursor()
    cur.execute(sql)
    con.close()

#####################################################################################################
#####################################################################################################
#####################################################################################################
###############################       PRACTICE            ###########################################
#####################################################################################################
#####################################################################################################
def coalesce2():
    array1 = [[1,"Old Name1",3],[2,"Old Name2",3],[3,"Old Name3",3],[4,"Old Name4",3],[1,"Old Name1",3],[2,"Old Name2",3],[3,"Old Name3",3],[4,"Old Name4",3]]
    array2 = [[2,"New Name2",3],[3,"New Name3",3]]
    # Create SparkSession
    spark = SparkSession.builder.master("local").appName("Practise").getOrCreate()
    # Create DF
    df1 = spark.createDataFrame(array1,["ID","Name","Score"])
    df2 = spark.createDataFrame(array2,["ID","Name"])
    df2_2 = df2.select("ID", col("Name").alias("Name_df2"))
    # JOIN task
    df3 = df1.join(df2_2, "ID", "left")
    # COALESCE task
    df4 = df3.withColumn("Name", coalesce("Name_df2","Name"))
    # order by
    df5 = df4.withColumn("ID2", func.row_number().over(Window.orderBy("ID")))
    df6 = df5.select("ID","Name", "Score")
    # Sum through groupBy
    df10 = df6.groupBy("ID","Name").sum("Score")
    df10.show()
    # SUM through agg
    df11 = df6.groupBy("ID","Name").agg(func.sum("Score").alias("Total_Score"))
    df11.show()

    df11 = df6.groupBy("ID","Name").agg(func.count("ID").alias("Total_Count"))
    df11.show()

    df11 = df6.groupBy("ID","Name").agg(func.count("ID").alias("Total_Count"),func.sum("Score").alias("Total_Score"))
    df11.show()
    spark.stop()
#coalesce2()

def coalesce3():
    spark = SparkSession.builder.master("local").appName("Coalesce3").getOrCreate()

    schema1 = StructType([StructField("ID",StringType(), True),
                         StructField("Name",StringType(), True),
                         StructField("Score",IntegerType(), True)])
    schema2 = StructType([StructField("ID",StringType(), True),
                         StructField("Name",StringType(), True)])

    array1 = [
        ["1", "Old_Name_1",1], ["2", "Old_Name_2",2], ["3", "Old_Name_3",3], ["4", "Old_Name_4",4],
        ["1", "Old_Name_1",1], ["2", "Old_Name_2",2], ["3", "Old_Name_3",3], ["4", "Old_Name_4",4]
    ]
    array2 = [["2","New_Name_2"],["3","New_Name_3"]]

    df1 = spark.createDataFrame(array1, schema1)
    print("df1=")
    df1.show()
    df2 = spark.createDataFrame(array2, schema2)
    print("df2=")
    df2.show()

    df1.createOrReplaceTempView("df1_table")
    df2.createOrReplaceTempView("df2_table")
    sql = """
    select df1.ID, coalesce(df2.Name, df1.Name) as Name, Score from df1_table df1 
    left join df2_table df2 on df1.ID=df2.ID
    order by df1.ID
    """
    df3 = spark.sql(sql)
    print("df3=")
    df3.show()

    df3.createOrReplaceTempView("df3_table")
    sql2 = """
    select ID, Name, count(ID) as count, sum(Score) as sum from df3_table group by ID, Name order by ID
    """
    df4 = spark.sql(sql2)
    print("df4=")
    df4.show()

    df4.createOrReplaceTempView("df4_table")
    sql3 = """
    select ID, Name, count, sum, 
    count(ID) over () as total_count, 
    sum(sum) over() as total_sum, 
    row_number() over(order by ID) as number
    from df4_table
    order by ID 
    """
    df5 = spark.sql(sql3)
    print("Total stats df5=")
    df5.show()

    #############################################################################
    df2_2 = df2.withColumnRenamed("Name","Name_df2")
    df6 = df1.join(df2_2, "ID", "left")
    df7 = df6.withColumn("Name", coalesce("Name_df2", "Name")).select("ID","Name","Score").orderBy("ID")
    print("df7=")
    df7.show()
    df8 = df7.groupBy("ID","Name").agg(func.count("ID").alias("count"),func.sum("Score").alias("sum")).orderBy("ID")
    print("df8=")
    df8.show()
    df9 = df8.withColumn("Total_Count", func.count("ID").over(Window.orderBy()))
    print("df9=")
    df9.show()
    df10 = df9.withColumn("Total_Sum", func.sum("sum").over(Window.orderBy()))
    print("df10=")
    df10.show()
    df11 = df10.withColumn("Number", func.row_number().over(Window.orderBy("ID")))
    print("df11=")
    df11.show()
    
    spark.stop()

#coalesce3()

