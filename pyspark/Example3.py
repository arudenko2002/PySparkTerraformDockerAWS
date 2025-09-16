'''
Created on Dec 6, 2018

@author: Alexey
'''
from pyspark import SparkContext, SparkConf
from pyspark import SparkFiles

from pyspark.sql import SparkSession #Main entry point for DataFrame and SQL functionality.
from pyspark.sql import DataFrame #A distributed collection of data grouped into named columns.
from pyspark.sql import Column #A column expression in a DataFrame.
from pyspark.sql import Row #A row of data in a DataFrame.
from pyspark.sql import GroupedData #Aggregation methods, returned by DataFrame.groupBy().
from pyspark.sql import DataFrameNaFunctions #Methods for handling missing data (null values).
from pyspark.sql import DataFrameStatFunctions #Methods for statistics functionality.
from pyspark.sql import functions #List of built-in functions available for DataFrame.
from pyspark.sql import types #List of data types available.
from pyspark.sql import Window #For working with window functions.

from datetime import datetime

def proba0():
    a=["xb","yc","za"]
    b = sorted(a, key = lambda x: x[1], reverse=True)
    print(b)
    d = "2016-01-01T03:03:03"
    dd = datetime.strptime(d,"%Y-%m-%dT%H:%M:%S")
    print(dd)
    bins = [ [] ] * 5
    bins2=[[],[]]
    print(bins)
    print(bins2)
    words = ['one', 'three', 'rough', 'sad', 'goof']
    #bins[0].append("aaa")
    bins2[0].append("NNN")
    for ind in bins2:
        print(ind)    
    
    for word in words:
        print(word)
        print(len(word)-1)
        print(bins[len(word)-1])
        bins[len(word)-1].append(word)
    
        for ind in bins:
            print(ind)
    #  How to delete from the list iterating through it(!).  Use copy l[:].  Gotcha..         
    l = list(range(10))
    print("L=",l)
    print("LL=",l[:])
    for item in l[:]:
        l.remove(item)
        print(l)
        print(l[:])
    print("L==",l)
    print("LL==",l[:])
    # sorted array
    l = [10,0,1,9,2,8,3,7,4,6,5]
    d = {"10":"5","0":"7"}
    print("or array=",l)
    print("D=",d)
    print("d items = ",d.items())
    
    import operator
    ll = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
    print("sorted array=",ll)
    
    ll2 = sorted(d.items(), key=lambda kv: kv[0])
    print("sorted array2=",ll2)
    
def proba():
    spark = SparkSession.builder \
    .master("local") \
    .appName("Word Count") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    df = spark.createDataFrame([([2, 1, None, 3],),([1],),([],)], ['data2'])
    print("SOURCE=",df.collect())
    result = df.select(functions.size(df.data2)).collect()
    print ("RESULT=\n",result)
    for ind in result:
        print ("Result=\n",ind)
    result2 = df.select(df.data2).collect()
    print ("RESULT2=\n",result2)
    for ind in result2:
        print ("Result2=\n",ind.data2)
        for ind2 in ind.data2:
            print ("Result3=",ind2)
    spark.stop()
        
def proba2():
    spark = SparkSession.builder \
    .master("local") \
    .appName("Word Count") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    df = spark.createDataFrame([('abcd',)], ['s',])
    r = df.select(functions.rpad(df.s, 6, '#').alias('s')).collect()
    print ("RESULT=", r)
    for ind in r:
        print ("Result=\n",ind)
        
    r2 = df.select(df.s.alias("alex")).collect()
    print("again1=",r2)
    for ind in r2:
        # list Row elements:
        for ind2 in ind:
            print ("again2=",ind2)
    spark.stop()

# Does not work "sequence"  Why???
def proba3():
    spark = SparkSession.builder \
    .master("local") \
    .appName("Word Count") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    df1 = spark.createDataFrame([(-2, 2)], ('C1', 'C2'))
    r1 = df1.select(functions.sequence('C1', 'C2').alias('r')).collect()
    print ("r1=",r1)
    #[Row(r=[-2, -1, 0, 1, 2])]
    df2 = spark.createDataFrame([(4, -4, -2)], ('C1', 'C2', 'C3'))
    r2 = df2.select(functions.sequence('C1', 'C2', 'C3').alias('r')).collect()
    print ("r2=",r2)
    #[Row(r=[4, 2, 0, -2, -4])]
    spark.stop()
    
def readDataArray():
    task = "Read_Date_Array"
    config = SparkConf().setAppName(task)
    sc = SparkContext(conf=config)
    data = sc.parallelize([("a","b","c"),("d","e","f"),("g","h","i"),("j","k","l")])
    print ("source_data=\n",data.collect())
    spark = SparkSession.builder \
    .master("local") \
    .appName(task) \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    df = spark.createDataFrame(data,("f1","f2","f3"))
    print ("df=\n",df.collect())
    df2 = df.select("f1","f2","f3").filter(df.f2=="k")
    print ("df2=\n",df2.collect())
    df.createOrReplaceTempView("table1")
    df3 = spark.sql("SELECT f1 AS field1, f2 as field2 from table1 where f2='e'")
    print ("df3=\n",df3.collect())
    sc.stop()
    
def readDataTest():
    def parse_N_calculate_age(data):
        (userid,age,gender,occupation,zip) = str(data).split("|")
        return  userid, gender,occupation,zip,int(age)
    task = "Read_Date_Text"
    config = SparkConf().setAppName(task)
    sc = SparkContext(conf=config)
    data = None #sc.textFile("C:\Users\Alexey\workspace\PySpark\PySpark\user.txt").map(parse_N_calculate_age)
    print ("source_data=\n",data.collect())
    spark = SparkSession.builder \
    .master("local") \
    .appName(task) \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    users = spark.createDataFrame(data,("userid", "gender","occupation","zip","age"))
    print ("users=\n",users.collect())
    users_50 = users.select("userid", "gender","occupation","zip","age").filter(users.age<50)
    print ("users_50=\n",users_50.collect())
    users.createOrReplaceTempView("table1")
    user_males= spark.sql("SELECT userid AS id, gender as gender, age as age from table1 where gender='M'")
    print ("users_males=\n",user_males.collect())
    spark.stop()
    
def readDataFrame():
    spark = SparkSession.builder \
    .master("local") \
    .appName("readDataFrame") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    from pyspark.sql.types import StructType, StructField, IntegerType, StringType

    schema = StructType([
        StructField("userid", IntegerType(), True),
        StructField("age", IntegerType(), True),
        StructField("gender", StringType(), True),
        StructField("occupation", StringType(), True),
        StructField("zip", StringType(), True)])
    
    users = None #spark.read.csv("C:\Users\Alexey\workspace\PySpark\PySpark\user.txt", sep="|", schema=schema)
    for ind in users.collect():
        print ("source_data=",ind)

    users_50 = users.select("userid", "gender","occupation","zip","age").filter(users.age<50)
    for ind in users_50.collect():
        print ("users_50=",ind)
        
        
    users.createOrReplaceTempView("table1")
    users_males= spark.sql("SELECT userid AS id, gender as gender, age as age from table1 where gender='M'")
    for ind in users_males.collect():
        print ("users_males=",ind)
    
    gender_count= spark.sql("SELECT gender,count(gender) as count  from table1 GROUP BY gender HAVING count>5")
    for ind in gender_count.collect():
        print ("gender_count=",ind)
        
    window_functions= spark.sql("SELECT userid AS id, occupation, gender as gender, age as age, LAG(age,1) OVER (partition by occupation order by occupation,age) as window from table1 where gender='M'")
    for ind in window_functions.collect():
        print ("windows function=",ind)

    spark.stop()
        
def employees():
    spark = SparkSession.builder \
    .master("local") \
    .appName("readDataFrame") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    from pyspark.sql.types import StructType, StructField, IntegerType, StringType

    schema = StructType([
        StructField("userid", IntegerType(), True),
        StructField("department", StringType(), True),
        StructField("salary", IntegerType(), True),
        StructField("gender",StringType(),True),
        StructField("occupation", StringType(), True),
        StructField("zip", StringType(), True)])
    
    users = None #spark.read.csv("C:\Users\Alexey\workspace\PySpark\PySpark\employees.txt", sep="|", schema=schema)
    for ind in users.collect():
        print ("source_data=",ind)
                
    users.createOrReplaceTempView("table1")
    window_functions1 = spark.sql("SELECT userid, occupation, department, salary from from table1 ORDER BY department,salary desc")
    for ind in window_functions1.collect():
        print ("e1=",ind)
        
    window_functions2= spark.sql("SELECT id, occupation, department, salary from (SELECT userid AS id, occupation, department, salary, rank(salary) OVER (partition by department order by department,salary DESC rows between unbounded preceding and current row) as window from table1) where window=2")
    for ind in window_functions2.collect():
        print ("e2=",ind)

    spark.stop()
        
def employeesFullScreen():
    spark = SparkSession.builder \
    .master("local") \
    .appName("readDataFrame") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    from pyspark.sql.types import StructType, StructField, IntegerType, StringType

    schema = StructType([
        StructField("userid", IntegerType(), True),
        StructField("department", StringType(), True),
        StructField("salary", IntegerType(), True),
        StructField("gender",StringType(),True),
        StructField("occupation", StringType(), True),
        StructField("zip", StringType(), True)])
    
    users = None #spark.read.csv("C:\Users\Alexey\workspace\PySpark\PySpark\employees.txt", sep="|", schema=schema)
    for ind in users.collect():
        print ("source_data=",ind)
                
    users.createOrReplaceTempView("table1")
    users.createOrReplaceTempView("table2")
    window_functions1 = spark.sql("SELECT distinct userid from (select userid from table1 UNION select userid from table2) order by userid")
    for ind in window_functions1.collect():
        print ("e1=",ind)

    spark.stop()
        
def employeesFullScreen2():
    #config = SparkConf().setAppName("aaaa")
    #sc = SparkContext(conf=config)
    #spark = SparkSession.builder.config(sc.getConf).getOrCreate()
    spark = SparkSession.builder \
    .master("local") \
    .appName("readDataFrame") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    from pyspark.sql.types import StructType, StructField, IntegerType, StringType

    schema = StructType([
        StructField("userid", IntegerType(), True),
        StructField("department", StringType(), True),
        StructField("salary", IntegerType(), True),
        StructField("gender",StringType(),True),
        StructField("occupation", StringType(), True),
        StructField("zip", StringType(), True)])
    
    users = None #spark.read.csv("C:\Users\Alexey\workspace\PySpark\PySpark\employees.txt", sep="|", schema=schema)
    #for ind in users.collect():
    #    print "source_data=",ind
    users2 = None #spark.read.csv("C:\Users\Alexey\workspace\PySpark\PySpark\employees.txt", sep="|", schema=schema)
    #for ind in users2.collect():
    #    print "source_data2=",ind
        
    users.createOrReplaceTempView("table1")
    users2.createOrReplaceTempView("table2")
    users3 = users.union(users2)
    users3.createOrReplaceTempView("table3")
    #for ind in users3.collect():
    #    print "source_data3=",ind
        
    window_functions1 = spark.sql("SELECT distinct userid from (select userid from table1 UNION select userid from table2) order by userid")
    #for ind in window_functions1.collect():
    #    print "e1=",ind
        
    window_functions2 = spark.sql("SELECT userid,department,salary,gender,occupation,zip from (select * from table1 UNION select * from table2) group by 1,2,3,4,5,6 ORDER BY userid")
    #for ind in window_functions2.collect():
    #    print "e2=",ind
    #window_functions2.show()
    users.show()
    users2.show()
    print("Add dataframes and get rid of doubles")
    import pyspark.sql.functions as fn
    distinct = users.union(users2).union(users3).groupBy(users3.columns[0:]).agg(fn.count('userid').alias('count')).orderBy('userid')
    distinct = users.union(users2).union(users3).groupBy(users3.columns[0:]).agg({}).orderBy('userid')
    #print(distinct)
    distinct.show()
    #for ind in distinct.collect():
    #    print "source_data3=",ind
    spark.stop()
    
def postgres():
    from pyspark.sql import SQLContext
    from pyspark.sql import DataFrameReader
    config = SparkConf().setAppName("Posrgres")
    sc = SparkContext(conf=config)
    sql_context = SQLContext(sc)   
    url = 'postgresql://127.0.0.1:5432/campaign_finance'
    properties = {'user': 'postgres', 'password': 'Mart1914', 'driver': 'org.postgresql.Driver'}
    df = DataFrameReader(sql_context).jdbc(
      url='jdbc:%s' % url, table='industry_codes', properties=properties
    )
    df.createOrReplaceTempView('table')
    df5=sql_context.sql('select * from table limit 5')
    df5.show()
    sc.stop()

    
def visitors():
    spark = SparkSession.builder \
    .master("local") \
    .appName("readDataFrame") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType

    schema = StructType([
        StructField("date", DateType(), True),
        StructField("app", StringType(), True),
        StructField("visitor_id", StringType(), True),
        StructField("visits_count",IntegerType(),True)])
    
    users = spark.read.csv("C:\\Users\\Alexey\\workspace\\PySpark\\PySpark\\visits.txt", sep="|", schema=schema)
    users.show()
    users.createOrReplaceTempView("visits")
    f=open("query.sql")
    sql = f.read()
    f.close()
#     sql="""
#     select date, count(1) as unique_visits_fullscreen 
#     FROM (
#         select date,app,visitor_id 
#         from visits 
#         where app=='Fullscreen' 
#         group by 1,2,3 
#         ORDER BY date,visitor_id
#     ) a 
#     group by 1 
#     having date<='2019-01-05' and date>DATE_SUB('2019-01-05',3) 
#     ORDER BY date DESC
#     """
    visits = spark.sql(sql)
    visits.show()
    spark.stop()

        
        
def yyy2(b_airports,y):
    return " ".join(x for x in b_airports.value[y])
def yyy(b_airports,y):
    return list(b_airports.value[y])[0]

def broadcastJoin():
    config=SparkConf().setAppName("BroadcastJson")
    sc = SparkContext(conf=config)
    # Fact table
    flights = sc.parallelize([
  ("SEA", "JFK", "DL", "418",  "7:00"),
  ("SFO", "LAX", "AA", "1250", "7:05"),
  ("SFO", "JFK", "VX", "12",   "7:05"),
  ("JFK", "LAX", "DL", "424",  "7:10"),
  ("LAX", "SEA", "DL", "5737", "7:10")])  
    print ("flights=\n", flights.collect())
   
    # Dimension table
    airports = sc.parallelize([
  ("JFK", "John F. Kennedy International Airport", "New York", "NY"),
  ("LAX", "Los Angeles International Airport", "Los Angeles", "CA"),
  ("SEA", "Seattle-Tacoma International Airport", "Seattle", "WA"),
  ("SFO", "San Francisco International Airport", "San Francisco", "CA")])
    print ("airports=\n", airports.collect())
   
    # Dimension table
    airlines = sc.parallelize([
  ("AA", "American Airlines"), 
  ("DL", "Delta Airlines"), 
  ("VX", "Virgin America")]) 
    print ("airlines=\n", airlines.collect() ) 
    
    b_airports = sc.broadcast(airports.map(lambda a: (a[0],a[2])).groupByKey().collectAsMap())
    print ("b_airports=\n",b_airports)
    b_airlines = sc.broadcast(airlines.groupByKey().collectAsMap())
    print ("b_airlines=\n",b_airlines)
    
    result = flights.map(lambda y: (yyy(b_airports,y[0]), yyy(b_airports,y[1]), yyy(b_airlines,y[2]), y[3], y[4]))
    print ("broadcast_join=\n", result.collect())
    sc.stop()
    
def broadcastJoinDataFrame():
    config=SparkConf().setAppName("BroadcastJson")
    sc = SparkContext(conf=config)
    # Fact table
    flights = sc.parallelize([
  ("SEA", "JFK", "DL", "418",  "7:00"),
  ("SFO", "LAX", "AA", "1250", "7:05"),
  ("SFO", "JFK", "VX", "12",   "7:05"),
  ("JFK", "LAX", "DL", "424",  "7:10"),
  ("LAX", "SEA", "DL", "5737", "7:10")])  
    print ("flights=\n", flights.collect())
   
    # Dimension table
    airports = sc.parallelize([
  ("JFK", "John F. Kennedy International Airport", "New York", "NY"),
  ("LAX", "Los Angeles International Airport", "Los Angeles", "CA"),
  ("SEA", "Seattle-Tacoma International Airport", "Seattle", "WA"),
  ("SFO", "San Francisco International Airport", "San Francisco", "CA")])
    print ("airports=\n", airports.collect())
   
    # Dimension table
    airlines = sc.parallelize([
  ("AA", "American Airlines"), 
  ("DL", "Delta Airlines"), 
  ("VX", "Virgin America")]) 
    print ("airlines=\n", airlines.collect())  
    
    spark = SparkSession.builder \
    .master("local") \
    .appName("readDataFrame") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
    
    from pyspark.sql.types import StructType, StructField, IntegerType, StringType
    schema_flights = StructType([
        StructField("airport_source", StringType(), True),
        StructField("airport_dest", StringType(), True),
        StructField("airline_id", StringType(), True),
        StructField("id", StringType(), True),
        StructField("departure", StringType(), True)])
    flights_df = spark.createDataFrame(flights,schema_flights)
    flights_df.registerTempTable('flights')
    flights_df.show()
    schema_airlines = StructType([
        StructField("airline_id", StringType(), True),
        StructField("airline", StringType(), True)])
    airlines_df = spark.createDataFrame(airlines,schema_airlines)
    airlines_df.registerTempTable('airlines')
    airlines_df.show()
    schema_airports = StructType([
        StructField("airport_id", StringType(), True),
        StructField("airport", StringType(), True),
        StructField("city", StringType(), True),
        StructField("state", StringType(), True)])
    airports_df = spark.createDataFrame(airports,schema_airports)
    airports_df.registerTempTable('airports')
    airports_df.show()
    data_joined_1 = flights_df.join(functions.broadcast(airlines_df), flights_df.airline_id == airlines_df.airline_id)
    data_joined_1.show()
    data_joined_2 = data_joined_1.join(functions.broadcast(airports_df), data_joined_1.airport_source == airports_df.airport_id) \
        .select(airports_df.city.alias('source'),data_joined_1.airport_dest,data_joined_1.airline, data_joined_1.id,airports_df.state,data_joined_1.departure)
    data_joined_2.show()
    data_joined_2.registerTempTable("table1")
    data_joined_3 = spark.sql("select source,airports.city as dest, airline, id, table1.state, departure from table1,airports where airport_dest == airport_id")
    #data_joined_3 = data_joined_2.join(airports_df, data_joined_2.airport_dest == airports_df.airport_id, 'inner')
    data_joined_3.show()
    for ind in data_joined_3.collect():
        print ("joined_data=",ind)
    list2 = list(data_joined_3.collect())
    print ("aaaaaaa \n",list2[0])
    print ("bbbbbbb \n",list2[1])
    print ("ccccccc \n",list2[2])
    print ("ddddddd \n",list2[3])
    print ("eeeeeee \n",list2[3]["source"])
    print ("fffffff \n",list2[3]["dest"])
    
    
    
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

    
      #initialize the spark session 
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
    #postgres driver needed
    import psycopg2
    #Amazon Redshift connect string 
    conn_string = "dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"  
    #connect to Redshift (database should be open to the world)
    con = psycopg2.connect(conn_string);
    
    #fiction variaBLES
    to_table=""
    fn=""
    delim=""
    quote=""
    gzip=""
    AWS_ACCESS_KEY_ID=""
    AWS_SECRET_ACCESS_KEY=""
    # end of fiction variables
    sql="""COPY %s FROM '%s' credentials 'aws_access_key_id=%s; aws_secret_access_key=%s' delimiter '%s' FORMAT CSV %s %s; commit;""" % (to_table, fn, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY,delim,quote,gzip)
    
    #Here
    #  fn - s3://path_to__input_file.gz
    #  gzip = 'gzip'
    
    cur = con.cursor()
    cur.execute(sql)
    con.close() 
    
if __name__ == '__main__':
    # proba0()
    # proba()
    #proba2()
    #proba3()
    #readDataArray()
    #readDataFrame()
    #employees()
    #broadcastJoin()
    broadcastJoinDataFrame()
    exit(0)
    #employeesFullScreen()
    #employeesFullScreen2()
    #visitors()
    #postgres()