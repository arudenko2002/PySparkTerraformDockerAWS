Implementation of Connection with a Database through JDBC
1. Create user, give him permission to read/write tables, create tables, etc.
username: "pyspark_user"
password: 'pysparkYEAR':

CREATE LOGIN pyspark_user WITH PASSWORD = 'pyspark2025';
use probe;
CREATE USER pyspark_user FOR LOGIN pyspark_user;
EXEC sp_addrolemember 'db_datareader', 'pyspark_user';
EXEC sp_addrolemember 'db_datawriter', 'pyspark_user';
EXEC sp_addrolemember 'db_ddladmin', 'pyspark_user';
--DROP USER pyspark_user;

select * from woven_users;
select * from woven_transactions;
--drop table woven_transactions;

-- truncate table woven_transactions;
2. Switch from "Windows Authentication" to "SQL Server and Windows Authentication"
3. Restart Server
4. Download mssql-jdbc-12.10.1.jre8.jar
5. Add line:
conf = SparkConf().setAppName(appName).setMaster(master).set("spark.driver.extraClassPath",
                                                                 "C:\\Users\\AlexR\\sqljdbc_12.10.1.0_enu\\sqljdbc_12.10\\enu\\jars\\mssql-jdbc-12.10.1.jre8.jar")

6. To read database, pyspark code:

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