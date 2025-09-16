from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, DateType, TimestampType
from pyspark.sql.functions import quarter, col, sum
from pyspark import SparkContext, SparkConf, SQLContext

class user_quarter:
    appName = "PySpark SQL Server Example - via JDBC"
    master = "local"
    conf = SparkConf().setAppName(appName).setMaster(master).set("spark.driver.extraClassPath",
                                                                 "C:\\Users\\AlexR\\sqljdbc_12.10.1.0_enu\\sqljdbc_12.10\\enu\\jars\\mssql-jdbc-12.10.1.jre8.jar")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    spark = sqlContext.sparkSession
    schema_transactions = StructType([
        StructField("transaction_id",IntegerType(),True),
        StructField("date", StringType(), True),
        StructField("amount", StringType(),True)
        ])
    schema_users = StructType([
        StructField("id",IntegerType(),True),
        StructField("name", StringType(), True),
        StructField("transaction_id", IntegerType(),True)
        ])

    schema_events = StructType([
        StructField("timestamp",TimestampType(),True),
        StructField("user_id", IntegerType(), True),
        StructField("event_id", StringType(),True),
        StructField("event_name", StringType(), True),
        StructField("info", StringType(), True)
        ])

    # def get_data_csv(self):
    #     df_users = self.spark.read.csv("users.csv",header=True, schema=self.schema_users)
    #     #df_users.show()
    #     df_transactions = self.spark.read.csv("transactions.csv", header=True, schema=self.schema_transactions)
    #     #df_transactions.show()
    #     return df_users, df_transactions

    def read_csv(self, filename, schema, header):
        return self.spark.read.csv(filename,header=header, schema=schema)

    def read_jdbc(self, table):
        database = "Probe"
        user = "pyspark_user"
        password = "pyspark2025"
        df = self.spark.read.format("jdbc") \
            .option("url",
                    f"jdbc:sqlserver://localhost:1433;databaseName={database};encrypt=true;trustServerCertificate=true") \
            .option("dbtable", table) \
            .option("user", user) \
            .option("password", password) \
            .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
            .load()
        print("jdbc=")
        df.show()
        return df

    def read_jdbc_with_query(self, table):
        database = "Probe"
        user = "pyspark_user"
        password = "pyspark2025"
        query = f"""(select * from {table} where transaction_id=6) as custom_query"""
        df = self.spark.read.format("jdbc") \
            .option("url",
                    f"jdbc:sqlserver://localhost:1433;databaseName={database};encrypt=true;trustServerCertificate=true") \
            .option("dbtable", query) \
            .option("user", user) \
            .option("password", password) \
            .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
            .load()
        print("jdbc=")
        df.show()
        return df

    def quarter_user(self, df_users, df_transactions, user=-1, quarter_num=-1):
        t_df = df_transactions.filter(quarter("date")==quarter_num)
        # print("t_df")
        # t_df.show()
        u_df = df_users.filter(col("id")==user)
        # print("u_df")
        # u_df.show()
        df_users_transactions = u_df.join(t_df,"transaction_id","inner")
        # print("df_users_transactions")
        # df_users_transactions.show()
        # df_users_transactions.printSchema()
        df = df_users_transactions.groupBy("id","name").agg(sum("amount").alias("quarterly_total"))
        print("result")
        df.show()
        return df

    def write_database(self, df, table):
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
        df.write.jdbc(
            url=jdbc_url,
            table=table,  # Schema and table name
            mode="append",  # Options: append, overwrite, ignore, error
            properties=connection_properties
        )

    def write_parquet(self, df, filename):
        df.write.parquet(filename)

    def read_parquet(self, filename):
        return self.spark.read.parquet(filename)


if __name__=="__main__":
    uq = user_quarter()
    #### df_events = uq.read_csv("..\\..\\ageoflearning_test\\events.csv", uq.schema_events)
    #### uq.write_database(df_events, "eol_events")
    df_users = uq.read_csv("users.csv", uq.schema_users, True)
    df_transactions = uq.read_csv("transactions.csv", uq.schema_transactions, True)
    # uq.write_parquet(df_users.coalesce(1), "users.parquet")
    # uq.write_parquet(df_transactions.coalesce(1), "transactions.parquet");
    # df_users = uq.read_parquet("users.parquet")
    # df_transactions = uq.read_parquet("transactions.parquet")
    # uq.write_database(df_users, "woven_users")
    # uq.write_database(df_transactions, "woven_transactions")
    # df_users = uq.read_jdbc("woven_users")
    # df_transactions = uq.read_jdbc_with_query("woven_transactions")
    df = uq.quarter_user(df_users, df_transactions, user=102, quarter_num=2)
