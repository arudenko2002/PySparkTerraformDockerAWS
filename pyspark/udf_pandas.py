from pyspark import SparkContext, SparkConf
from pyspark import SparkFiles
from typing import Iterator
import pyspark.sql.functions as func
from pyspark.sql.functions import col, coalesce, sum as _sum, desc, udf, explode, arrays_zip, flatten
from pyspark.sql.types import IntegerType, FloatType,  ArrayType, StringType
from pyspark.sql.types import StructType, StructField
from pyspark.sql import Window


from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from pyspark.sql.functions import pandas_udf, PandasUDFType
import pandas as pd
from pyspark.sql.functions import pandas_udf
import pyarrow as pap
import requests
import json



def udf_pandas0():
    spark = SparkSession.builder \
        .master("local") \
        .appName("readDataFrame") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    df = spark.createDataFrame([
        ("ID1", 'string11', 1),
        ("ID1", 'string12', 2),
        ("ID1", 'string13', 3),
        ("ID2", 'string21', 4),
        ("ID2", 'string22', 5),
        ("ID2", 'string23', 6),
        ("ID3", 'string31', 7),
        ("ID3", 'string32', 8),
        ("ID3", 'string33', 9),
    ], schema='ID string, VALUE string, VALUE2 int')
    df.show()

    print(pap.__version__)
    #from scipy import stats
    # @pandas_udf('double')
    # def cdf(v):
    #     return pd.Series(stats.norm.cdf(v))
    # Use pandas_udf to define a Pandas UDF
    from typing import Iterator
    return spark, df
    #return pd.DataFrame([3, 5, 'store123', 'product123', 'My log message'], columns=['y', 'ds','store_id','product_id', 'log'])
from pyspark.sql.types import IntegerType
#multiply = udf(pandas_plus_one, returnType=IntegerType())

def udf_pandas1():
    spark, df = udf_pandas0()
    df3 = df.select(["VALUE2"])
    df3.show()

    @pandas_udf("int")
    def pandas_plus_one(data):
        return data * data
    #df2 = df3.select(multiply(col("VALUE2")))
    df2 = df3.toPandas()

    data = {'VALUE2': [1, 2, 3]}
    pandas_df = pd.DataFrame(data)

    print(type(df2))
    print(type(pandas_df))
    print(type(df3))
    a = pandas_df["VALUE2"].apply(lambda x: x*x)
    print(a)
    b = df3.withColumn("v22",pandas_plus_one(col("VALUE2")))
    print(b)
    b.printSchema()
    b.collect()
    b.show()
# udf_pandas1()

def udf_pandas2():
    spark = SparkSession.builder \
        .master("local") \
        .appName("readDataFrame") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    array1 = [
        ["1", "Name1", 1],
        ["1", "Name1", 2],
        ["1", "Name1", 3],
        ["2", "Name2", 10],
        ["2", "Name2", 20],
        ["2", "Name2", 30],
        ["3", "Name3", 100],
        ["3", "Name3", 200],
        ["3", "Name3", 300]
    ]
    array2 = ["ID","Name", "Score"]
    df = spark.createDataFrame(array1, array2)
    #df.show()

    # df2 = df.groupBy("ID","Name").agg(func.count("ID"), func.sum("Score")).orderBy("ID")
    # df2.show()

    #@udf("long")
    def f(k, x):
        print(x)
        print(type(x), x)
        a = 0
        for val in list(x):
            a += val
        print(x)
        print(type(x))
        print(a)
        return 1.0*a/len(x)

    myUdf = udf(f, FloatType())

    df3 = df.groupBy("ID", "Name").agg(func.sum("Score").alias("summa")).withColumn("V2", col("summa"))
    df3.show()

    df.groupby('ID').applyInPandas(f, schema="ID string, Score double").show()


    # df3= df.withColumn("V2",plus_one("Score"))
    # df3.show()

# udf_pandas2()

def udf_pandas3():
    conf = SparkConf()
    conf.set("spark.driver.extraJavaOptions", "-Dio.netty.tryReflectionSetAccessible=true")
    conf.set("spark.executor.extraJavaOptions", "-Dio.netty.tryReflectionSetAccessible=true")

    # conf = {"spark.driver.extraJavaOptions":
    #             "-Dio.netty.tryReflectionSetAccessible=true",
    #         "spark.executor.extraJavaOptions":
    #             "-Dio.netty.tryReflectionSetAccessible=true"
    #         }

    spark = SparkSession.builder \
        .master("local") \
        .appName("readDataFrame") \
        .config(conf=conf) \
        .getOrCreate()
    @udf("string")
    def to_upper(s: pd.Series) -> pd.Series:
        print(type(s), len(s))
        a=[]
        return s.split()
        # for ss in s:
        #     a.append(ss.upper())
        # return a

    df = spark.createDataFrame([("John Doe",),("Jane Joe",)], ("name",))
    print("df_udf_pandas3=")
    df.show()
    df.select(to_upper("name")).show()

    from typing import Iterator
    @udf("long")
    def plus_one(iterator: Iterator[pd.Series]) -> Iterator[pd.Series]:
        # out = []
        # for s in iterator:
        #     out.append(s + 1)
        # return out
        return iterator+1

    df2 = spark.createDataFrame(pd.DataFrame([1, 2, 3], columns=["v"]))
    print("df2_udf_pandas3=")
    df2.select(plus_one(df.v)).show()

    array1 = [
        ["1", "Name1", 1],
        ["1", "Name1", 2],
        ["1", "Name1", 3],
        ["2", "Name2", 10],
        ["2", "Name2", 20],
        ["2", "Name2", 30],
        ["3", "Name3", 100],
        ["3", "Name3", 200],
        ["3", "Name3", 300]
    ]
    array2 = ["ID","Name", "Score"]
    df3 = spark.createDataFrame(array1, array2)
    print("df3_udf_pandas3=")
    df3.show()
    df4 = df.withColumn("number", func.row_number().over(Window.orderBy("ID")) % 3)
    print("df_udf_pandas4=")
    df4.show()
    df5 = df4.groupBy("number").agg(func.collect_list("name").alias("values_array"))
    print("df5_udf_pandas3=")
    df5.show()

    def api(s: pd.Series) -> pd.Series:
        #print(type(s))
        address = "http://localhost:8080/api/?urls="+s[0]
        for ind in range(1,len(s)):
            #print(s[ind], type(s[ind]))
            address += "+" + s[ind]
        # print(address)
        r = requests.get(address)
        data = r.json()
        # data2 = r.text
        # data = json.loads(data2)
        return data

    api_udf = udf(api, ArrayType(StringType()))


    df6 = df5.withColumn("response", api_udf("values_array")) #.select("values_array","response")
    print("df6_udf_pandas3=")
    df6.show()

    df44 = df6.withColumn("bc", arrays_zip("values_array","response"))
    df44.show()
    df45 = df44.select("number", explode("bc").alias("tbc"))
    df45.show()
    df46 = df45.select("number", "tbc.values_array", "tbc.response")
    df46.show()
    df47 = df46.orderBy("values_array")
    df47.show()
    exit()

    df5 = df6.withColumn("url", explode("values_array")).select("url")
    df5.show()
    df4.printSchema()
    df6= df4.withColumn("enrich", explode("response")).select("enrich")
    df6.show()
    df7 = df5.rdd.zip(df6.rdd).toDF(["url","enrich"])
    df7.show()

    df8 = df7.withColumn("url", col("url.url")).withColumn("enrich", col("enrich.enrich"))
    df8.show()

    df9 = df8.groupBy("url","enrich").agg(func.count(col("url"))).select("url", "enrich")
    df9.show()

    df10 = df.join(df9, col("name")==col("url"), "inner")
    df10.show()

    df11 = df10.drop("url")
    df11.show()

# udf_pandas3()

def udf_pandas4():
    conf = SparkConf()
    conf.set("spark.driver.extraJavaOptions", "-Dio.netty.tryReflectionSetAccessible=true")
    conf.set("spark.executor.extraJavaOptions", "-Dio.netty.tryReflectionSetAccessible=true")

    spark = SparkSession.builder \
        .master("local") \
        .appName("readDataFrame") \
        .config(conf=conf) \
        .getOrCreate()

    array1 = [
        ["1", "Name1", 1],
        ["1", "Name1", 2],
        ["1", "Name1", 3],
        ["2", "Name2", 10],
        ["2", "Name2", 20],
        ["2", "Name2", 30],
        ["3", "Name3", 100],
        ["3", "Name3", 200],
        ["3", "Name3", 300],
        ["4", "Name4", 1000],
        ["4", "Name4", 2000],
        ["4", "Name4", 3000],
        ["5", "Name5", 10000],
        ["5", "Name5", 20000],
        ["5", "Name5", 30000]
    ]
    array2 = ["ID","Name", "Score"]
    df = spark.createDataFrame(array1, array2)
    print("df=")
    df.show()
    df2 = df.withColumn("number", func.row_number().over(Window.orderBy("ID")) % 3)
    #print("df2=")
    #df2.show()
    df3 = df2.groupBy("number").agg(func.collect_list("name").alias("values_array"), func.collect_list("score").alias("score_array"))
    print("df3=")
    df3.show(truncate=False)

    def api(s: pd.Series) -> pd.Series:
        #print(type(s))
        address = "http://localhost:8080/api/?urls="+s[0]
        for ind in range(1,len(s)):
            #print(s[ind], type(s[ind]))
            address += "+" + s[ind]
        # print(address)
        r = requests.get(address)
        data = r.json()
        # data2 = r.text
        # data = json.loads(data2)
        return data

    #def my_pandas(s: pd.Series) -> pd.Series:
    def my_pandas(t, s):
        # print(t,type(t))
        # print(s,type(s))
        df = pd.DataFrame(s, columns=['Fruit'])
        # print("pdf=")
        # print(df)
        # print("dfnum=", df.to_numpy())
        # print("num0=", df.to_numpy()[0])
        # print(s==df.to_numpy())
        # print(df.sum())
        # print("loc=",df.loc[0])
        # print("iloc=", df.iloc[0])
        # print("loc=",df.loc[1])
        # print("iloc=", df.iloc[1])
        # print("loc=",df.loc[2])
        # print("iloc=", df.iloc[2])

        df.iloc[0] += 1
        df.iloc[1] += 5
        df.iloc[2] += 25
        df.loc[0] += 1
        df.loc[1] += 5
        df.loc[2] += 25
        df2 = pd.DataFrame(t, columns=['Vegies'])
        zf = pd.DataFrame(zip(df2['Vegies'], df['Fruit']), columns=['Veg', 'Fr'])
        print("zf=")
        print(zf)
        #zf["Salad"] = zf["Veg"]+" "+str(zf["Fr"])
        #zf = df.assign(Salad=zf['Veg'] + " "+str(zf['Fr']))
        zf['Salad'] = zf.apply(lambda x: x['Veg'] + " " + str(x['Fr']), axis=1)
        print("zf=")
        print(zf)
        #return df['Fruit'].to_list()
        return zf["Salad"].to_list()

    api_udf = udf(api, ArrayType(StringType()))
    pandas_udf = udf(my_pandas, ArrayType(StringType()))


    df4 = df3.withColumn("response", api_udf("values_array"))
    print("df4=")
    df4.show(truncate=False)

    df4 = df3.withColumn("response", pandas_udf("values_array", "score_array"))
    print("df4=")
    df4.show(truncate=False)

    df44 = df4.withColumn("bc", arrays_zip("values_array","response"))
    print("df44=")
    df44.show(truncate=False)
    df45 = df44.select("number", explode("bc").alias("tbc"))
    print("df45=")
    df45.show(truncate=False)
    df46 = df45.select("number", "tbc.values_array", "tbc.response")
    print("df46=")
    df46.show(truncate=False)
    df47 = df46.orderBy("values_array")
    print("df47=")
    df47.show(truncate=False)

    df5 = df47.filter(col("number")==0)  # can be 0, 1, 2
    print("df5=")
    df5.show()
    print("df= again")
    df.show()
    df6 = df.join(df5, df.Name==df5.values_array,"inner").select("ID", "Name","Score","response")
    print("df6=")
    df6.show()

#udf_pandas4()

"""
df=
+---+-----+-----+
| ID| Name|Score|
+---+-----+-----+
|  1|Name1|    1|
|  1|Name1|    2|
|  1|Name1|    3|
|  2|Name2|   10|
|  2|Name2|   20|
|  2|Name2|   30|
|  3|Name3|  100|
|  3|Name3|  200|
|  3|Name3|  300|
+---+-----+-----+

df3=  func.collect_list("name") column to list field
+------+---------------------+------------+
|number|values_array         |score_array |
+------+---------------------+------------+
|1     |[Name1, Name2, Name3]|[1, 10, 100]|
|2     |[Name1, Name2, Name3]|[2, 20, 200]|
|0     |[Name1, Name2, Name3]|[3, 30, 300]|
+------+---------------------+------------+

df4=
+------+---------------------+------------+------------------------------+
|number|values_array         |score_array |response                      |
+------+---------------------+------------+------------------------------+
|1     |[Name1, Name2, Name3]|[1, 10, 100]|[Name1_L1, Name2_L2, Name3_L3]|
|2     |[Name1, Name2, Name3]|[2, 20, 200]|[Name1_L1, Name2_L2, Name3_L3]|
|0     |[Name1, Name2, Name3]|[3, 30, 300]|[Name1_L1, Name2_L2, Name3_L3]|
+------+---------------------+------------+------------------------------+

df4=
+------+---------------------+------------+------------------------------+
|number|values_array         |score_array |response                      |
+------+---------------------+------------+------------------------------+
|1     |[Name1, Name2, Name3]|[1, 10, 100]|[Name1 3, Name2 20, Name3 150]|
|2     |[Name1, Name2, Name3]|[2, 20, 200]|[Name1 4, Name2 30, Name3 250]|
|0     |[Name1, Name2, Name3]|[3, 30, 300]|[Name1 5, Name2 40, Name3 350]|
+------+---------------------+------------+------------------------------+

zf=
     Veg   Fr
0  Name1    5
1  Name2   40
2  Name3  350
zf=
     Veg   Fr      Salad
0  Name1    5    Name1 5
1  Name2   40   Name2 40
2  Name3  350  Name3 350

df44=
+------+---------------------+------------+------------------------------+---------------------------------------------------------+
|number|values_array         |score_array |response                      |bc                                                       |
+------+---------------------+------------+------------------------------+---------------------------------------------------------+
|1     |[Name1, Name2, Name3]|[1, 10, 100]|[Name1 3, Name2 20, Name3 150]|[{Name1, Name1 3}, {Name2, Name2 20}, {Name3, Name3 150}]|
|2     |[Name1, Name2, Name3]|[2, 20, 200]|[Name1 4, Name2 30, Name3 250]|[{Name1, Name1 4}, {Name2, Name2 30}, {Name3, Name3 250}]|
|0     |[Name1, Name2, Name3]|[3, 30, 300]|[Name1 5, Name2 40, Name3 350]|[{Name1, Name1 5}, {Name2, Name2 40}, {Name3, Name3 350}]|
+------+---------------------+------------+------------------------------+---------------------------------------------------------+

df45=
+------+------------------+
|number|tbc               |
+------+------------------+
|1     |{Name1, Name1 3}  |
|1     |{Name2, Name2 20} |
|1     |{Name3, Name3 150}|
|2     |{Name1, Name1 4}  |
|2     |{Name2, Name2 30} |
|2     |{Name3, Name3 250}|
|0     |{Name1, Name1 5}  |
|0     |{Name2, Name2 40} |
|0     |{Name3, Name3 350}|
+------+------------------+

df46=
+------+------------+---------+
|number|values_array|response |
+------+------------+---------+
|1     |Name1       |Name1 3  |
|1     |Name2       |Name2 20 |
|1     |Name3       |Name3 150|
|2     |Name1       |Name1 4  |
|2     |Name2       |Name2 30 |
|2     |Name3       |Name3 250|
|0     |Name1       |Name1 5  |
|0     |Name2       |Name2 40 |
|0     |Name3       |Name3 350|
+------+------------+---------+

df47=
+------+------------+---------+
|number|values_array|response |
+------+------------+---------+
|1     |Name1       |Name1 3  |
|2     |Name1       |Name1 4  |
|0     |Name1       |Name1 5  |
|1     |Name2       |Name2 20 |
|2     |Name2       |Name2 30 |
|0     |Name2       |Name2 40 |
|1     |Name3       |Name3 150|
|2     |Name3       |Name3 250|
|0     |Name3       |Name3 350|
+------+------------+---------+

df5=
+------+------------+---------+
|number|values_array| response|
+------+------------+---------+
|     0|       Name1|  Name1 5|
|     0|       Name2| Name2 40|
|     0|       Name3|Name3 350|
+------+------------+---------+

df= again
+---+-----+-----+
| ID| Name|Score|
+---+-----+-----+
|  1|Name1|    1|
|  1|Name1|    2|
|  1|Name1|    3|
|  2|Name2|   10|
|  2|Name2|   20|
|  2|Name2|   30|
|  3|Name3|  100|
|  3|Name3|  200|
|  3|Name3|  300|
+---+-----+-----+

df6=
+---+-----+-----+---------+
| ID| Name|Score| response|
+---+-----+-----+---------+
|  2|Name2|   10| Name2 40|
|  2|Name2|   20| Name2 40|
|  2|Name2|   30| Name2 40|
|  1|Name1|    1|  Name1 5|
|  1|Name1|    2|  Name1 5|
|  1|Name1|    3|  Name1 5|
|  3|Name3|  100|Name3 350|
|  3|Name3|  200|Name3 350|
|  3|Name3|  300|Name3 350|
+---+-----+-----+---------+
"""


# Start Flask server code2/cli_or_serve_fastapi.py
def udf_pandas5():
    spark = SparkSession.builder.master("local").appName("readDataFrame").config("spark.some.config.option", "some-value").getOrCreate()
    array1 = [
        ["1", "Name1", 1],
        ["1", "Name1", 2],
        ["1", "Name1", 3],
        ["2", "Name2", 10],
        ["2", "Name2", 20],
        ["2", "Name2", 30],
        ["3", "Name3", 100],
        ["3", "Name3", 200],
        ["3", "Name3", 300],
        ["4", "Name4", 1000],
        ["4", "Name4", 2000],
        ["4", "Name4", 3000],
        ["5", "Name5", 10000],
        ["5", "Name5", 20000],
        ["5", "Name5", 30000]
    ]
    array2 = ["ID","Name", "Score"]
    df = spark.createDataFrame(array1, array2)
    print("df=")
    df.show()

    df2 = df.withColumn("number",(func.row_number().over(Window.orderBy('ID'))/4).cast(IntegerType()))
    print("df2=")
    df2.show()

    df3 = df2.groupBy("number").agg(func.collect_list("Name").alias("name_array"), func.collect_list("Score").alias("score_array"))
    print("df3=")
    df3.show()
    # Start Flask server code2/cli_or_serve_fastapi.py
    def api(s: pd.Series) -> pd.Series:
        #print(type(s))
        address = "http://localhost:8080/api/?urls="+s[0]
        for ind in range(1,len(s)):
            #print(s[ind], type(s[ind]))
            address += "+" + s[ind]
        # print(address)
        r = requests.get(address)
        data = r.json()
        # data2 = r.text
        # data = json.loads(data2)
        return data

    #def my_pandas(s: pd.Series) -> pd.Series:
    def my_pandas(t, s):
        print(t,type(t))
        print(s,type(s))
        df = pd.DataFrame(s, columns=['Fruit'])
        df.iloc[0] += 1
        df.iloc[1] += 5
        df.iloc[2] += 25
        df.loc[0] += 1
        df.loc[1] += 5
        df.loc[2] += 25
        df2 = pd.DataFrame(t, columns=['Vegies'])
        zf = pd.DataFrame(zip(df2['Vegies'], df['Fruit']), columns=['Veg', 'Fr'])
        print("zf=")
        print(zf)
        #zf["Salad"] = zf["Veg"]+" "+str(zf["Fr"])
        #zf = df.assign(Salad=zf['Veg'] + " "+str(zf['Fr']))
        zf['Salad'] = zf.apply(lambda x: x['Veg'] + " " + str(x['Fr']), axis=1)
        print("zf=")
        print(zf)
        #return df['Fruit'].to_list()
        return zf["Salad"].to_list()

    api_udf = udf(api, ArrayType(StringType()))
    pandas_udf = udf(my_pandas, ArrayType(StringType()))

    df4 = df3.withColumn("url_response", api_udf(col("name_array"))).alias("url_response")
    print("df4=")
    df4.show()

    df5 = df3.withColumn("pandas_response", pandas_udf(col("name_array"), col("score_array"))).alias("pandas_response")
    print("df5=")
    df5.show()

    df6 = df5.withColumn("zipped_result", func.arrays_zip("name_array", "pandas_response"))
    print("df6=")
    df6.show()

    df7 = df6.select("number", explode("zipped_result").alias("exploded_result"))
    print("df7=")
    df7.show()

    df8 = df7.select("number",col("exploded_result.name_array").alias("name"), col("exploded_result.pandas_response").alias("pandas_score"))
    print("df8=")
    df8.show()

    # we select "max score" obtained from Pandas
    df9 = df8.groupBy("name").agg(func.max("pandas_score").alias("max_pandas_score"))
    print("df9=")
    df9.show()

    df10 = df.join(df9, "name","inner")
    print("df10=")
    df10.show()

    df60 = df4.withColumn("zipped_result", func.arrays_zip("name_array", "url_response"))
    print("df60=")
    df60.show()

    df70 = df60.select("number", explode("zipped_result").alias("exploded_result"))
    print("df70=")
    df70.show()

    df80 = df70.select("number", col("exploded_result.name_array").alias("name"),
                     col("exploded_result.url_response").alias("url_score"))
    print("df80=")
    df80.show()

    # we select "max score" obtained from URL
    df90 = df80.groupBy("name").agg(func.max("url_score").alias("max_url_score"))
    print("df90=")
    df90.show()

    df100 = df10.join(df90, "name", "inner")
    print("df100=")
    df100.orderBy("Name").show()



#udf_pandas5()

"""

df=
+---+-----+-----+
| ID| Name|Score|
+---+-----+-----+
|  1|Name1|    1|
|  1|Name1|    2|
|  1|Name1|    3|
|  2|Name2|   10|
|  2|Name2|   20|
|  2|Name2|   30|
|  3|Name3|  100|
|  3|Name3|  200|
|  3|Name3|  300|
|  4|Name4| 1000|
|  4|Name4| 2000|
|  4|Name4| 3000|
|  5|Name5|10000|
|  5|Name5|20000|
|  5|Name5|30000|
+---+-----+-----+

df2=
+---+-----+-----+------+
| ID| Name|Score|number|
+---+-----+-----+------+
|  1|Name1|    1|     0|
|  1|Name1|    2|     0|
|  1|Name1|    3|     0|
|  2|Name2|   10|     1|
|  2|Name2|   20|     1|
|  2|Name2|   30|     1|
|  3|Name3|  100|     1|
|  3|Name3|  200|     2|
|  3|Name3|  300|     2|
|  4|Name4| 1000|     2|
|  4|Name4| 2000|     2|
|  4|Name4| 3000|     3|
|  5|Name5|10000|     3|
|  5|Name5|20000|     3|
|  5|Name5|30000|     3|
+---+-----+-----+------+

df3=
+------+--------------------+--------------------+
|number|          name_array|         score_array|
+------+--------------------+--------------------+
|     0|[Name1, Name1, Na...|           [1, 2, 3]|
|     1|[Name2, Name2, Na...|   [10, 20, 30, 100]|
|     2|[Name3, Name3, Na...|[200, 300, 1000, ...|
|     3|[Name4, Name5, Na...|[3000, 10000, 200...|
+------+--------------------+--------------------+

df4=
+------+--------------------+--------------------+--------------------+
|number|          name_array|         score_array|        url_response|
+------+--------------------+--------------------+--------------------+
|     0|[Name1, Name1, Na...|           [1, 2, 3]|[Name1_L1, Name1_...|
|     1|[Name2, Name2, Na...|   [10, 20, 30, 100]|[Name2_L1, Name2_...|
|     2|[Name3, Name3, Na...|[200, 300, 1000, ...|[Name3_L1, Name3_...|
|     3|[Name4, Name5, Na...|[3000, 10000, 200...|[Name4_L1, Name5_...|
+------+--------------------+--------------------+--------------------+

df5=
/////  This is Pandas output
['Name1', 'Name1', 'Name1'] <class 'list'>
[1, 2, 3] <class 'list'>
zf=
     Veg  Fr
0  Name1   3
1  Name1  12
2  Name1  53
zf=
     Veg  Fr     Salad
0  Name1   3   Name1 3
1  Name1  12  Name1 12
2  Name1  53  Name1 53
['Name2', 'Name2', 'Name2', 'Name3'] <class 'list'>
[10, 20, 30, 100] <class 'list'>
zf=
     Veg   Fr
0  Name2   12
1  Name2   30
2  Name2   80
3  Name3  100
zf=
     Veg   Fr      Salad
0  Name2   12   Name2 12
1  Name2   30   Name2 30
2  Name2   80   Name2 80
3  Name3  100  Name3 100
['Name3', 'Name3', 'Name4', 'Name4'] <class 'list'>
[200, 300, 1000, 2000] <class 'list'>
zf=
     Veg    Fr
0  Name3   202
1  Name3   310
2  Name4  1050
3  Name4  2000
zf=
     Veg    Fr       Salad
0  Name3   202   Name3 202
1  Name3   310   Name3 310
2  Name4  1050  Name4 1050
3  Name4  2000  Name4 2000
['Name4', 'Name5', 'Name5', 'Name5'] <class 'list'>
[3000, 10000, 20000, 30000] <class 'list'>
zf=
     Veg     Fr
0  Name4   3002
1  Name5  10010
2  Name5  20050
3  Name5  30000
zf=
     Veg     Fr        Salad
0  Name4   3002   Name4 3002
1  Name5  10010  Name5 10010
2  Name5  20050  Name5 20050
3  Name5  30000  Name5 30000
/////  End of Pandas output
+------+--------------------+--------------------+--------------------+
|number|          name_array|         score_array|     pandas_response|
+------+--------------------+--------------------+--------------------+
|     0|[Name1, Name1, Na...|           [1, 2, 3]|[Name1 3, Name1 1...|
|     1|[Name2, Name2, Na...|   [10, 20, 30, 100]|[Name2 12, Name2 ...|
|     2|[Name3, Name3, Na...|[200, 300, 1000, ...|[Name3 202, Name3...|
|     3|[Name4, Name5, Na...|[3000, 10000, 200...|[Name4 3002, Name...|
+------+--------------------+--------------------+--------------------+

df6=
+------+--------------------+--------------------+--------------------+--------------------+
|number|          name_array|         score_array|     pandas_response|       zipped_result|
+------+--------------------+--------------------+--------------------+--------------------+
|     0|[Name1, Name1, Na...|           [1, 2, 3]|[Name1 3, Name1 1...|[{Name1, Name1 3}...|
|     1|[Name2, Name2, Na...|   [10, 20, 30, 100]|[Name2 12, Name2 ...|[{Name2, Name2 12...|
|     2|[Name3, Name3, Na...|[200, 300, 1000, ...|[Name3 202, Name3...|[{Name3, Name3 20...|
|     3|[Name4, Name5, Na...|[3000, 10000, 200...|[Name4 3002, Name...|[{Name4, Name4 30...|
+------+--------------------+--------------------+--------------------+--------------------+

df7=
+------+--------------------+
|number|     exploded_result|
+------+--------------------+
|     0|    {Name1, Name1 3}|
|     0|   {Name1, Name1 12}|
|     0|   {Name1, Name1 53}|
|     1|   {Name2, Name2 12}|
|     1|   {Name2, Name2 30}|
|     1|   {Name2, Name2 80}|
|     1|  {Name3, Name3 100}|
|     2|  {Name3, Name3 202}|
|     2|  {Name3, Name3 310}|
|     2| {Name4, Name4 1050}|
|     2| {Name4, Name4 2000}|
|     3| {Name4, Name4 3002}|
|     3|{Name5, Name5 10010}|
|     3|{Name5, Name5 20050}|
|     3|{Name5, Name5 30000}|
+------+--------------------+

df8=
+------+-----+------------+
|number| name|pandas_score|
+------+-----+------------+
|     0|Name1|     Name1 3|
|     0|Name1|    Name1 12|
|     0|Name1|    Name1 53|
|     1|Name2|    Name2 12|
|     1|Name2|    Name2 30|
|     1|Name2|    Name2 80|
|     1|Name3|   Name3 100|
|     2|Name3|   Name3 202|
|     2|Name3|   Name3 310|
|     2|Name4|  Name4 1050|
|     2|Name4|  Name4 2000|
|     3|Name4|  Name4 3002|
|     3|Name5| Name5 10010|
|     3|Name5| Name5 20050|
|     3|Name5| Name5 30000|
+------+-----+------------+

df9=
+-----+----------------+
| name|max_pandas_score|
+-----+----------------+
|Name1|        Name1 53|
|Name2|        Name2 80|
|Name3|       Name3 310|
|Name4|      Name4 3002|
|Name5|     Name5 30000|
+-----+----------------+

df10=
+-----+---+-----+----------------+
| Name| ID|Score|max_pandas_score|
+-----+---+-----+----------------+
|Name2|  2|   10|        Name2 80|
|Name2|  2|   20|        Name2 80|
|Name2|  2|   30|        Name2 80|
|Name5|  5|10000|     Name5 30000|
|Name5|  5|20000|     Name5 30000|
|Name5|  5|30000|     Name5 30000|
|Name1|  1|    1|        Name1 53|
|Name1|  1|    2|        Name1 53|
|Name1|  1|    3|        Name1 53|
|Name4|  4| 1000|      Name4 3002|
|Name4|  4| 2000|      Name4 3002|
|Name4|  4| 3000|      Name4 3002|
|Name3|  3|  100|       Name3 310|
|Name3|  3|  200|       Name3 310|
|Name3|  3|  300|       Name3 310|
+-----+---+-----+----------------+

df60=
+------+--------------------+--------------------+--------------------+--------------------+
|number|          name_array|         score_array|        url_response|       zipped_result|
+------+--------------------+--------------------+--------------------+--------------------+
|     0|[Name1, Name1, Na...|           [1, 2, 3]|[Name1_L1, Name1_...|[{Name1, Name1_L1...|
|     1|[Name2, Name2, Na...|   [10, 20, 30, 100]|[Name2_L1, Name2_...|[{Name2, Name2_L1...|
|     2|[Name3, Name3, Na...|[200, 300, 1000, ...|[Name3_L1, Name3_...|[{Name3, Name3_L1...|
|     3|[Name4, Name5, Na...|[3000, 10000, 200...|[Name4_L1, Name5_...|[{Name4, Name4_L1...|
+------+--------------------+--------------------+--------------------+--------------------+

df70=
+------+-----------------+
|number|  exploded_result|
+------+-----------------+
|     0|{Name1, Name1_L1}|
|     0|{Name1, Name1_L2}|
|     0|{Name1, Name1_L3}|
|     1|{Name2, Name2_L1}|
|     1|{Name2, Name2_L2}|
|     1|{Name2, Name2_L3}|
|     1|{Name3, Name3_L4}|
|     2|{Name3, Name3_L1}|
|     2|{Name3, Name3_L2}|
|     2|{Name4, Name4_L3}|
|     2|{Name4, Name4_L4}|
|     3|{Name4, Name4_L1}|
|     3|{Name5, Name5_L2}|
|     3|{Name5, Name5_L3}|
|     3|{Name5, Name5_L4}|
+------+-----------------+

df80=
+------+-----+---------+
|number| name|url_score|
+------+-----+---------+
|     0|Name1| Name1_L1|
|     0|Name1| Name1_L2|
|     0|Name1| Name1_L3|
|     1|Name2| Name2_L1|
|     1|Name2| Name2_L2|
|     1|Name2| Name2_L3|
|     1|Name3| Name3_L4|
|     2|Name3| Name3_L1|
|     2|Name3| Name3_L2|
|     2|Name4| Name4_L3|
|     2|Name4| Name4_L4|
|     3|Name4| Name4_L1|
|     3|Name5| Name5_L2|
|     3|Name5| Name5_L3|
|     3|Name5| Name5_L4|
+------+-----+---------+

df90=
+-----+-------------+
| name|max_url_score|
+-----+-------------+
|Name1|     Name1_L3|
|Name2|     Name2_L3|
|Name3|     Name3_L4|
|Name4|     Name4_L4|
|Name5|     Name5_L4|
+-----+-------------+

df100=
+-----+---+-----+----------------+-------------+
| Name| ID|Score|max_pandas_score|max_url_score|
+-----+---+-----+----------------+-------------+
|Name1|  1|    1|        Name1 53|     Name1_L3|
|Name1|  1|    2|        Name1 53|     Name1_L3|
|Name1|  1|    3|        Name1 53|     Name1_L3|
|Name2|  2|   10|        Name2 80|     Name2_L3|
|Name2|  2|   20|        Name2 80|     Name2_L3|
|Name2|  2|   30|        Name2 80|     Name2_L3|
|Name3|  3|  100|       Name3 310|     Name3_L4|
|Name3|  3|  200|       Name3 310|     Name3_L4|
|Name3|  3|  300|       Name3 310|     Name3_L4|
|Name4|  4| 1000|      Name4 3002|     Name4_L4|
|Name4|  4| 2000|      Name4 3002|     Name4_L4|
|Name4|  4| 3000|      Name4 3002|     Name4_L4|
|Name5|  5|10000|     Name5 30000|     Name5_L4|
|Name5|  5|20000|     Name5 30000|     Name5_L4|
|Name5|  5|30000|     Name5 30000|     Name5_L4|
+-----+---+-----+----------------+-------------+

"""

def udf_pandas6():
    spark = SparkSession.builder.master("local").appName("readDataFrame").config("spark.some.config.option", "some-value").getOrCreate()
    array1 = [
        ["1", "Name1", {"a":"1", "b":"2","c":"3", "d":[1,2,3], "fruit":{"apple":1, "pear":2}}],
    ]

    #data = [("1", '{"name": "Alice", "age": 25}'), ("2", '{"name": "Bob", "age": 30}')]
    array2 = ["ID","Name", "Score"]
    df = spark.createDataFrame(array1, array2)
    print("df=")
    df.show()
    df.select("Score", "Score.a", "Score.b", "Score.c").show()
    df2 = df.select("ID","Name","Score", explode(df.Score))
    df2.show()
    json_schema = StructType([
        StructField("apple", IntegerType(), True),
        StructField("pear", IntegerType(), True)
    ])

udf_pandas6()

