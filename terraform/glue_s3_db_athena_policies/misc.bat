aws sts get-caller-identity
@REM aws sts get-caller-identity
@REM {
@REM     "UserId": "AIDA5LMSVKH6VAEITRTTV",
@REM     "Account": "917819970045",
@REM     "Arn": "arn:aws:iam::917819970045:user/user1"
@REM }

aws glue get-table --database-name source_database --name source_table

@REM  aws glue get-table --database-name source_database --name source_table
@REM {
@REM     "Table": {
@REM         "Name": "source_table",
@REM         "DatabaseName": "source_database",
@REM         "CreateTime": "2025-08-10T18:30:04-07:00",
@REM         "UpdateTime": "2025-08-10T18:30:04-07:00",
@REM         "Retention": 0,
@REM         "StorageDescriptor": {
@REM             "Columns": [
@REM                 {
@REM                     "Name": "name",
@REM                     "Type": "string",
@REM                     "Comment": "",
@REM                     "Parameters": {}
@REM                 },
@REM                 {
@REM                     "Name": "title",
@REM                     "Type": "string",
@REM                     "Comment": "",
@REM                     "Parameters": {}
@REM                 },
@REM                 {
@REM                     "Name": "amount",
@REM                     "Type": "int",
@REM                     "Comment": "",
@REM                     "Parameters": {}
@REM                 }
@REM             ],
@REM             "Location": "s3://alexey-source-bucket-input/data/",
@REM             "AdditionalLocations": [],
@REM             "InputFormat": "org.apache.hadoop.mapred.TextInputFormat",
@REM             "OutputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat",
@REM             "Compressed": false,
@REM             "NumberOfBuckets": 0,
@REM             "SerdeInfo": {
@REM                 "Name": "OpenCSVSerde",
@REM                 "SerializationLibrary": "org.apache.hadoop.hive.serde2.OpenCSVSerde"
@REM             },
@REM             "BucketColumns": [],
@REM             "SortColumns": [],
@REM             "Parameters": {},
@REM             "StoredAsSubDirectories": false
@REM         },
@REM         "PartitionKeys": [],
@REM         "TableType": "EXTERNAL_TABLE",
@REM         "CreatedBy": "arn:aws:iam::917819970045:user/user1",
@REM         "IsRegisteredWithLakeFormation": false,
@REM         "CatalogId": "917819970045",
@REM         "VersionId": "0"
@REM     }
@REM }

aws athena delete-work-group --work-group alexey_athena_destination_wg --recursive-delete-option

aws athena list-work-groups

aws athena start-query-execution --query-string "SELECT * FROM alexey_destination_db.destination_table" --work-group alexey_athena_query_results_wg --result-configuration OutputLocation="s3://alexey-athena-query-results-33407785/"

aws athena get-query-execution --query-execution-id 64df66b3-d61e-4985-a219-d047895f100a

aws athena get-query-results --query-execution-id 64df66b3-d61e-4985-a219-d047895f100a

aws configure list