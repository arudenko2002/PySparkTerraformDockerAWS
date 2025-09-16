'''
Created on Nov 9, 2018

@author: Alexey
'''
#spark-submit C:\Users\Alexey\workspace\PySpark\PySpark\Example1.py
from pyspark import SparkContext, SparkConf
from pyspark import SparkFiles

def parse_N_calculate_age(data):
    (userid,age,gender,occupation,zip) = data.split("|")
    return  userid, age_group(int(age)),gender,occupation,zip,int(age)

def  age_group(age):
    if age < 10 :
        return '0-10'
    elif age < 20:
        return '10-20'
    elif age < 30:
        return '20-30'
    elif age < 40:
        return '30-40'
    elif age < 50:
        return '40-50'
    elif age < 60:
        return '50-60'
    elif age < 70:
        return '60-70'
    elif age < 80:
        return '70-80'
    else :
        return '80+'
   
def outliers(data):
    global Over_age, Under_age
    age_grp = data[1]
    if(age_grp == "70-80"):
        Over_age +=1
    if(age_grp == "0-10"):
        Under_age +=1
    return data
       
if __name__ == '__main__':
    print("AAA")
    ##############Take(), First(), TakeSample(), count() ############################################################
    conf = SparkConf().setAppName('MyFirstStandaloneApp1')
    sc = SparkContext(conf=conf)
    RDDread = sc.textFile ("C:\\Users\\AlexR\\PycharmProjects\\pythonProject\\pyspark\\CHANGES.txt")
    print(RDDread.collect())
    print(RDDread.first())
    print(RDDread.take(5))
    print(RDDread.takeSample(False, 10, 2))
    print(RDDread.count())
    sc.stop()
    ##############Count, Join , distinct############################################################
    conf = SparkConf().setAppName('MyFirstStandaloneApp2')
    sc = SparkContext(conf=conf)
    Country = sc.textFile("C:\\Users\\AlexR\\PycharmProjects\\pythonProject\\pyspark\\Country.txt")
    CountryLanguage = sc.textFile("C:\\Users\\AlexR\\PycharmProjects\\pythonProject\\pyspark\\CountryLanguage.txt")
    print( "00000=", Country.count())
    print( "11111=", CountryLanguage.count())
    country_name = Country.map(lambda row:(row.split(" ")[0],row.split(" ")[1]))
    country_lang = CountryLanguage.map(lambda row : (row.split(" ")[0],row.split(" ")[1]))
    print( "00000=", country_name.count())
    print( "11111=", country_lang.count())
    Countryname_language = country_name.join(country_lang)
    print( "aaaaaaaaaaa ")
    print( Countryname_language.take(2))
    print( "bbbbbbbbbbb ")
    print( Countryname_language.distinct().count())
    sc.stop()
    ##############Take, Count, Collect(), Sample() Filter()###########################################################
    conf = SparkConf().setAppName('MyFirstStandaloneApp3')
    sc = SparkContext(conf=conf)
    confusedRDD = sc.textFile("C:\\Users\\AlexR\\PycharmProjects\\pythonProject\\pyspark\\confused.txt")
    mappedconfusion = confusedRDD.map(lambda line : line.split(" "))
    mappedconfusion.take(5)
    flatMappedConfusion = confusedRDD.flatMap(lambda line : line.split(" "))
    flatMappedConfusion.take(5)
    onlyconfusion = confusedRDD.filter(lambda line : ("confus" in line.lower()))
    print( "AAAAAAA ",onlyconfusion.count())
    print( "BBBBBBB ",onlyconfusion.collect())
    sampledconfusion = confusedRDD.sample(True,0.5,3) #True implies withReplacement
    print( "CCCCCCC ", str(sampledconfusion.collect()))
    sc.stop()
    #################textFile, filter, count########################################################
    conf = SparkConf().setAppName('MyFirstStandaloneApp4')
    sc = SparkContext(conf=conf) 
    changesRDD = sc.textFile(".\\CHANGES.txt")
    Daschanges = changesRDD.filter (lambda line: "tathagata.das1565@gmail.com" in line)
    print( "DDDDDDD ", Daschanges.count())
    ankurchanges = changesRDD.filter(lambda line : "hao.cheng@intel.com" in line)
    print( "EEEEEEE ", ankurchanges.count())
    sc.stop()
    ################Union, Join #########################################################
    conf = SparkConf().setAppName('MyFirstStandaloneApp5')
    sc = SparkContext(conf=conf) 
    abhay_marks = [("physics",85),("maths",75),("chemistry",95)] 
    ankur_marks = [("physics",65),("maths",45),("chemistry",85)]
    abhay = sc.parallelize(abhay_marks)
    ankur = sc.parallelize(ankur_marks)
    print( "FFFFFFFFF ", abhay.union(ankur).collect())
    Subject_wise_marks = abhay.join(ankur)
    print( "GGGGGGGGG ", Subject_wise_marks.collect())
    sc.stop()
    ##################Intersection #######################################################
    conf = SparkConf().setAppName('MyFirstStandaloneApp6')
    sc = SparkContext(conf=conf) 
    Cricket_team = ["sachin","abhay","michael","rahane","david","ross","raj","rahul","hussy","steven","sourav"]
    Toppers = ["rahul","abhay","laxman","bill","steve"]
    cricketRDD = sc.parallelize(Cricket_team)
    toppersRDD = sc.parallelize(Toppers)
    toppercricketers = cricketRDD.intersection(toppersRDD)
    print( "HHHHHHHHH ", toppercricketers.collect())
    sc.stop()
    ##################Union Union#######################################################
    conf = SparkConf().setAppName('MyFirstStandaloneApp7')
    sc = SparkContext(conf=conf) 
    best_story = ["movie1","movie3","movie7","movie5","movie8"]
    best_direction = ["movie11","movie1","movie5","movie10","movie7"]
    best_screenplay = ["movie10","movie4","movie6","movie7","movie3"]
    story_rdd = sc.parallelize(best_story)
    direction_rdd = sc.parallelize(best_direction)
    screen_rdd = sc.parallelize(best_screenplay)
    total_nomination_rdd = story_rdd.union(direction_rdd).union(screen_rdd)
    print( "IIIIIIII ", total_nomination_rdd.collect())
     
    unique_movies_rdd = total_nomination_rdd.distinct()
    print( "JJJJJJJJ ", unique_movies_rdd .collect())
    sc.stop()
    #################Cache() Persist()########################################################???????????????????????
    conf = SparkConf().setAppName('MyFirstStandaloneApp8')
    sc = SparkContext(conf=conf) 
    partRDD = sc.textFile("C:\\Users\\AlexR\\PycharmProjects\\pythonProject\\pyspark\\CHANGES.txt",4)
    print( "KKKKKKK ", partRDD.getNumPartitions())
    userRDD = sc.textFile("C:\\Users\\AlexR\\PycharmProjects\\pythonProject\\pyspark\\user.txt")
    print( "LLLLLLL ", userRDD.count())
    best_story = ["movie1","movie3","movie7","movie5","movie8"]
    words = sc.parallelize(best_story)
    words.cache() 
    caching = words.persist().is_cached 
    print( "Words got chached > %s" % (caching))
    sc.stop()
    #################Broadcast Value##########################################################????????????????????????
    conf = SparkConf().setAppName('MyFirstStandaloneApp9')
    sc = SparkContext("local", "Broadcast app") 
    words_new = sc.broadcast(["scala", "java", "hadoop", "spark", "akka"]) 
    data = words_new.value 
    print( "Stored data -> %s" % (data))
    elem = words_new.value[2] 
    print( "print(ing a particular element in RDD -> %s" % (elem))
    sc.stop()
    ###################CountByValue Accumulator Filter Map######################################################################?????????????????
    conf = SparkConf().setAppName('MyFirstStandaloneApp10').setMaster("local")
    sc = SparkContext(conf=conf)
    userRDD = sc.textFile("C:\\Users\\AlexR\\PycharmProjects\\pythonProject\\pyspark\\user.txt").cache()
    data_with_age_bucket = userRDD.map(parse_N_calculate_age)
    RDD_20_30 = data_with_age_bucket.filter(lambda line : '20-30' in line)
    freq = RDD_20_30.map(lambda line : line[3]).countByValue()
    print( "MMMMMMMMM total user count is ",userRDD.count())
    print( "NNNNNNNNN total movie users profession wise ",dict(freq))
    Under_age = sc.accumulator(0)
    Over_age = sc.accumulator(0)
    df = data_with_age_bucket.map(outliers).collect()
    print( "QQQQQQQQ ", df)
    print( "OOOOOOOOO  under age users of the movie are ",Under_age)
    print( "PPPPPPPPP  over age users of the movie are ",Over_age)
    sc.stop()
    
    #exit(0)
    ##################SparkFiles addFile#####################################################################???????????????????????
    finddistance = "recommend.py"
    path1="C:\\Users\\AlexR\\PycharmProjects\\pythonProject\\pyspark"
    import os
    path = os.path.join(path1, "recommend.py")
    print(path)
    sc = SparkContext("local", "SparkFile App")
    sc.addFile(path)
    # finddistancename = "finddistance.R"
    # print( "Absolute Path -> %s" % SparkFiles.get(finddistancename))
    sc.stop()
    ###############persist getStoragelevel ########################################################################??????????????????
    import pyspark
    sc = SparkContext (
       "local", 
       "storagelevel app"
    )
    rdd1 = sc.parallelize([1,2])
    rdd1.persist( pyspark.StorageLevel.MEMORY_AND_DISK_2 )
    rdd1.getStorageLevel()
    print(rdd1.getStorageLevel())
    sc.stop()
    ################Serializer######################################################################??????????????
    #Serializer for RDD
    from pyspark.context import SparkContext
    from pyspark.serializers import MarshalSerializer
    sc = SparkContext("local", "serialization app", serializer = MarshalSerializer())
    print(sc.parallelize(list(range(1000))).map(lambda x: 2 * x).take(10))
    sc.stop()
    ######################################################################################
#    pyspark.SparkContext().textFile("s3n://user:password@bucket/key")
#    rdd = sc.hadoopFile('s3n://my_bucket/my_file', conf = {
#       'fs.s3n.awsAccessKeyId': '...',
#       'fs.s3n.awsSecretAccessKey': '...',
#    })
    
#     bucket = "mycompany-mydata-bucket"
#     prefix = "2015/04/04/mybiglogfile.log.gz"
#     filename = "s3n://{}/{}".format(bucket, prefix)
#     
#     config_dict = {"fs.s3n.awsAccessKeyId":"FOOBAR",
#                    "fs.s3n.awsSecretAccessKey":"BARFOO"}
#     
#     rdd = sc.hadoopFile(filename,
#                         'org.apache.hadoop.mapred.TextInputFormat',
#                         'org.apache.hadoop.io.Text',
#                         'org.apache.hadoop.io.LongWritable',
#                         conf=config_dict)
    
#     import os
#     import configparser
#     
#     config = configparser.ConfigParser()
#     config.read(os.path.expanduser("~/.aws/credentials"))
#     
#     aws_profile = 'default' # your AWS profile to use
#     
#     access_id = config.get(aws_profile, "aws_access_key_id") 
#     access_key = config.get(aws_profile, "aws_secret_access_key") 
    
#     wordcounts = sc.textFile('hdfs://ubuntu1:54310/user/dev/gutenberg') \
#         .map( lambda x: x.replace(',',' ').replace('.',' ').replace('-',' ').lower()) \
#         .flatMap(lambda x: x.split()) \
#         .map(lambda x: (x, 1)) \
#         .reduceByKey(lambda x,y:x+y) \
#         .map(lambda x:(x[1],x[0])) \
#         .sortByKey(False) 
    #################################################################################
    pass