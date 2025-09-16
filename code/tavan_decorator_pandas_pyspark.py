"""
import flask
@route("/home",GET)
def function():
    return {'key': "value"}

count words

Python

l = [1,2,3,3,4]

m = dict()
for ind in l:
    if ind in m:
        m[ind] += 1
    else:
        m[ind] = 1

groupby()

print(m)

#customer_id
df1=
df2 = purcases of the customer

df3 = df1.join(df2,"customer_id","left")

df3.withColumn("another_column", func.coalesce("name", lit("Name of mine")))

Do the same with Pandas
pd.df3.apply()

SQL:

t1 emplyee  employee_id, employee_name department_id salary
t2 department department_id department_name



select department_name, employee_name, salary from employee e join (
select department_name,max(salary) from
(
select department_name, employee_name, salary from employee e join department d on e.departemnt_id=e.department_id
) t
group by deoartment_name)
) tt
on e.salary=r.salary and tt.department_name= e.departmnet_name

Snowflake

AWS  Lambda
"""
from symbol import decorator


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# def decor(func):
#     def wrapper():
#         print("step1")
#         func()
#         print("step2")
#     return wrapper
#
# @decor
# def f():
#     print("YES!!!")
# f()


# def my_own_decorator(func):
#     def wrapper():
#         print("somethong before")
#         func()
#         print("something after")
#     return wrapper
#
# @my_own_decorator
# def func2():
#     print("MYYYYYYYYYY")
#
# func2()

import pandas as pd
import numpy as np
def missing_data():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print("AAAAAAAAAA")
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
    print(df1)
    #                    A         B         C    D    F   E
    # 2013-01-01  0.000000  0.000000  1.000942  5.0  NaN NaN
    # 2013-01-02  1.021225  0.590646  1.025253  5.0  1.0 NaN
    # 2013-01-03 -0.113823  0.000807 -0.256247  5.0  2.0 NaN
    # 2013-01-04  1.586299  0.293922  0.183469  5.0  3.0 NaN
    df1.loc[dates[0] : dates[1], "E"] = 1
    print(df1)
    #                    A         B         C    D    F    E
    # 2013-01-01  0.000000  0.000000  0.609693  5.0  NaN  1.0
    # 2013-01-02  0.851869  0.962829  0.449798  5.0  1.0  1.0
    # 2013-01-03  0.523858  0.426518  1.774167  5.0  2.0  NaN
    # 2013-01-04  0.022128  2.684758  1.041568  5.0  3.0  NaN
    data = df1.dropna(how="any")
    print(data)
    #                    A        B         C    D    F    E
    # 2013-01-02 -1.207087 -0.36042  0.579986  5.0  1.0  1.0
    data = df1.fillna(value=5)
    print(data)
    #                    A         B         C    D    F    E
    # 2013-01-01  0.000000  0.000000  1.854734  5.0  5.0  1.0
    # 2013-01-02 -0.185308  0.431159 -0.350343  5.0  1.0  1.0
    # 2013-01-03 -1.235122 -1.738727  1.224550  5.0  2.0  5.0
    # 2013-01-04 -0.455281 -0.751144  0.404837  5.0  3.0  5.0
    data = pd.isna(df1)
    print(data)
    #                 A      B      C      D      F      E
    # 2013-01-01  False  False  False  False   True  False
    # 2013-01-02  False  False  False  False  False  False
    # 2013-01-03  False  False  False  False  False   True
    # 2013-01-04  False  False  False  False  False   True

missing_data()

def coalesce_example():
    dates = pd.date_range("20130101", periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
    print("AAAAAAAAAA")
    print(df)
    df.loc[dates[0]: dates[5], "D"] = 1
    print("df=")
    print(df)

    dates2 = pd.date_range("20130101", periods=3)
    df2 = pd.DataFrame(np.random.randn(3, 1), index=dates2, columns=["D2"])
    df2.loc[dates[0]: dates[5], "D2"] = 2
    print("df2=")
    print(df2)
 
    df3 = pd.merge(df, df2, how="left", left_on=dates, right_on=dates2)
    print("df3=")
    print(df3)

    df3['D3'] = df3.D2.combine_first(df3.D)
    print("df3 Coalesce")
    print(df3)

    df4 = df3.drop(columns=["D","D2"], axis=1)
    print("df4=")
    print(df4)

    df5 = df4.rename(columns={"D3":"D"})
    print("df5=")
    print(df5)

    df6 = df5.rename(columns={"key_0": ""})
    print("df6=")
    print(df6)

coalesce_example()


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, split, desc

def rdd_word_count():
    spark = SparkSession.builder \
    .master("local") \
    .appName("Word Count") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

    text_df = spark.read.text("word.txt")
    print("text_rdd=")
    text_df.show(truncate=False)

    text_rdd = text_df.rdd
    print("text_rdd=",text_rdd.collect())

    word_rdd = text_rdd.flatMap(lambda line: line.value.split(' '))
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