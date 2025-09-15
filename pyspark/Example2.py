#spark-submit C:\Users\Alexey\workspace\PySpark\PySpark\Example1.py
from pyspark import SparkContext, SparkConf
from pyspark import SparkFiles
import pyspark.sql.functions as func

#TRANSFORMATION
# //MAP
# println("MAP")
# val x= sc.parallelize(Array("b", "a", "c"))
# val y= x.map(z => (z,1))
# println(x.collect().mkString(", "))
# println(y.collect().mkString(", "))
# //x:['b', 'a', 'c']
# //y: [('b', 1), ('a', 1), ('c', 1)]
def map():
    print("Map")
    config = SparkConf().setAppName('Map')
    sc = SparkContext(conf=config) 
    old_data = ["a","b","c"] 
    data = sc.parallelize(old_data)
    print ("Source= ", data.collect())
    result = data.map(lambda x:(x,1))
    print ("Map result=",result.collect())

# //FILTER
# println("FILTER")
# val x= sc.parallelize(Array(1,2,3))
# val y= x.filter(n => n%2 == 1)
# println(x.collect().mkString(", "))
# println(y.collect().mkString(", "))
# //x:[1,2,3]
# //y:[1,3]    
def filter():
    print("Filter")
    config = SparkConf().setAppName("Filter")
    sc = SparkContext(conf=config)
    old_data=[1,2,3,4,5,6,7,8,9,10]
    data = sc.parallelize(old_data)
    result = data.filter(lambda x: x%2==0)
    print ("Filter result=\n", result.collect())

# //FLATMAP
# println("FLATMAP")
# val x= sc.parallelize(Array(1,2,3))
# val y= x.flatMap(n => Array(n, n*100, 42))
# println(x.collect().mkString(", "))
# println(y.collect().mkString(", "))
# //x:[1, 2, 3]
# //y: [1, 100, 42, 2, 200, 42, 3, 300, 42]    
def flatmap():
    print("Flatmap")
    config = SparkConf().setAppName("Flatmap")
    sc = SparkContext(conf=config)
    old_data = [1,2,3,4,5,6,7,8,9,10]
    data = sc.parallelize(old_data)
    map = data.map(lambda x: [x, 100 * x, 38])
    print("map", map.collect())
    result = data.flatMap(lambda x: [x,100*x,38] )
    print ("flatmap=\n", result.collect())

"""
map [[1, 100, 38], [2, 200, 38], [3, 300, 38], [4, 400, 38], [5, 500, 38], [6, 600, 38], [7, 700, 38], [8, 800, 38], [9, 900, 38], [10, 1000, 38]]
flatmap= [1, 100, 38, 2, 200, 38, 3, 300, 38, 4, 400, 38, 5, 500, 38, 6, 600, 38, 7, 700, 38, 8, 800, 38, 9, 900, 38, 10, 1000, 38]
"""

# //GROUPBY
# println("GROUPBY")
# val x= sc.parallelize(Array("John", "Fred", "Anna", "James"))
# val y= x.groupBy(w => w.charAt(0))
# println(x)
# println(y.collect().mkString(", "))
# //x:['John', 'Fred', 'Anna', 'James']
# //y:[('A',['Anna']),('J',['John','James']),('F',['Fred'])]    
def groupby():
    print("GroupBy")
    config = SparkConf().setAppName("GroupBy")
    sc = SparkContext(conf=config)
    old_data = ["John", "Fred", "Anna", "James"]
    data= sc.parallelize(old_data)
    print("data=",data.collect())
    result = data.groupBy(lambda x: x[0])
    result2 = result.collect()
    print("result2=", result2)
    for ind in result2:
        print ("groupby=",ind[0])
        print ("Names=",", ".join(ind[1]))
"""
result2= [('J', <pyspark.resultiterable.ResultIterable object at 0x00000136735BAA90>), ('F', <pyspark.resultiterable.ResultIterable object at 0x00000136735D0DF0>), ('A', <pyspark.resultiterable.ResultIterable object at 0x00000136735D0E50>)]
groupby= J
Names= John, James
groupby= F
Names= Fred
groupby= A
Names= Anna
"""

def groupby_countword():
    print("GroupBy")
    config = SparkConf().setAppName("GroupBy")
    sc = SparkContext(conf=config)
    old_data = ["John", "Fred", "Anna", "James", "Anna"]
    data= sc.parallelize(old_data)
    print("data=",data.collect())
    result = data.groupBy(lambda x: x).mapValues(len)
    print(result.collect())
"""
data= ['John', 'Fred', 'Anna', 'James', 'Anna']
[('Fred', 1), ('John', 1), ('James', 1), ('Anna', 2)]
"""

# //GROUPBYKEY
# println("GROUPBYKEY")
# val x= sc.parallelize(Array(('B',5),('B',4),('A',3),('A',2),('A',1)))
# val y= x.groupByKey()
# println(x.collect().mkString(", "))
# println(y.collect().mkString(", "))
# //x:[('B', 5),('B', 4),('A', 3),('A', 2),('A', 1)]
# //y:[('A', [2, 3, 1]),('B',[5, 4])]
# //z:{'A':iter([2,3],[20,30]),'B':iter([5,4])}
def groupbykey():
    print("GroupByKey")
    config = SparkConf().setAppName("GroupByKey")
    sc = SparkContext(conf=config)
    old_data = [('B',5),('B',4),('A',3),('A',2),('A',1)]
    old_data = [("A",[2,3]),("A",[20,30]),("B",[200,300])]
    data = sc.parallelize(old_data)
    result = data.groupByKey()
    result2 = result.collect()
    print ("groupbykey",result2)
    for ind in result2:
        print ("groupbykey1", ind[0])
        print ("groupbykey2=",(", ").join(str(x) for x in ind[1]))
        #for ind2 in ind[1]:
        #    print "groupbykey3=",ind2
    # collectAsMap: result is the dictionary with keys (keys are created by groupByKey)         
    result22 = result.collectAsMap()
    print ("groupbykey collectMap",result22)
    print ("CollectAsMap=\n\n\n\n",result.collectAsMap())
    for ind in result22:
        print ("groupbykey11", ind)
        #print "groupbykey22=",(", ").join(str(x) for x in result22[ind])
        print(type(result22[ind]))
        for ind2 in result22[ind]:
            print ("groupbykey3=",ind2)

# //REDUCEBYKEY VS. GROUPBYKEY
# println("REDUCEBYKEY VS. GROUPBYKEY")
# val words = Array("one", "two", "two", "three", "three", "three")
# val wordPairsRDD= sc.parallelize(words)C
# val wordCountsWithReduce= wordPairsRDD
# .reduceByKey(_ + _)
# .collect()
# val wordCountsWithGroup= wordPairsRDD
# .groupByKey()
# .map(t => (t._1, t._2.sum))
# .collect()
def strange(it):
    ar = [x for x in it]
    s=0
    for ind in ar:
        s += ind
    return s
def reducebykey_vs_groupbykey():
    config = SparkConf().setAppName("groupByKey")
    sc = SparkContext(conf=config)
    old_data = ["one", "two", "two", "three", "three", "three"]
    data = sc.parallelize(old_data).map(lambda x: (x,1))
    print("mapped dataset=", data.collect())
    # mapped dataset data = [('one', 1), ('two', 1), ('two', 1), ('three', 1), ('three', 1), ('three', 1)]
    result = data.reduceByKey(lambda x,y: x+y)
    print ("reducerbykey=\n",result.collect())
    # reducerbykey=
    # [('two', 2), ('three', 3), ('one', 1)]
    result2 = data.groupByKey() #.map(lambda x:(x[0],sum()))
    print ("groupbykey=\n",result2.collect())
    # groupbykey =
    # [('two', < pyspark.resultiterable.ResultIterable object at 0x0000028B6BF4CF40 >),
    #  ('three', < pyspark.resultiterable.ResultIterable object at 0x0000028B6BF4CFA0 >),
    #  ('one', < pyspark.resultiterable.ResultIterable object at 0x0000028B6BF57040 >)]
    result3 = result2.mapValues(len)
    print ("groupbykey.mapValues=\n",result3.collect())
    result4 = result2.mapValues(list)
    print ("result4 groupbykey.mapValues=\n",result4.collect())
    # sum was not working (overrun by another function called sum(fsum now).  strange is the function that substitute it, see strange above
    a=[1,2,3]
    print(type(a))
    b = sum(a)  #instead of sum, see above comment
    print(b)
    result5 = result2.mapValues(sum)
    print ("result5 groupbykey.mapValues=\n",result5.collect())
    # groupbykey.mapValues =
    # [('two', 2), ('three', 3), ('one', 1)]
    result3 = result2.map(lambda x: (x[0], strange(x[1])))
    print ("groupbykey.map=\n",result3.collect())
    # groupbykey.map =
    # [('two', 2), ('three', 3), ('one', 1)]


"""
mapped dataset= [('one', 1), ('two', 1), ('two', 1), ('three', 1), ('three', 1), ('three', 1)]
reducerbykey=
 [('two', 2), ('three', 3), ('one', 1)]
groupbykey=
 [('two', <pyspark.resultiterable.ResultIterable object at 0x0000028FF15A3370>), ('three', <pyspark.resultiterable.ResultIterable object at 0x0000028FF15AE430>), ('one', <pyspark.resultiterable.ResultIterable object at 0x0000028FF15AE490>)]
groupbykey.mapValues=
 [('two', 2), ('three', 3), ('one', 1)]
result4 groupbykey.mapValues=
 [('two', [1, 1]), ('three', [1, 1, 1]), ('one', [1])]
<class 'list'>
6
result5 groupbykey.mapValues=
 [('two', 2), ('three', 3), ('one', 1)]
groupbykey.map=
 [('two', 2), ('three', 3), ('one', 1)]
"""


#def f(partitionIndex:Int, i:Iterator[Int]) = {
#(partitionIndex, i.sum).productIterator
#}  

# //MAPPARTITIONS
# println("MAPPARTITIONS")
# val x= sc.parallelize(Array(1,2,3), 2)
# def f(i:Iterator[Int])={ (i.sum,42).productIterator}
# val y= x.mapPartitions(f)
# // glom() flattens elements on the same partition
# val xOut= x.glom().collect()
# val yOut= y.glom().collect()
# println(x)
# println(xOut)
# println(yOut)
# //x:Array(Array(1), Array(2, 3))
# //y:Array(Array(1, 42), Array(5, 42))
def mappartitions():
    config = SparkConf().setAppName("Mappartitions")
    sc = SparkContext(conf=config)
    data = sc.parallelize([1,2,3],2)
    def f(i):
        c=0
        for ii in i:
            c=c+ii
        return (c,42)
    result = data.mapPartitions(f)
    print ("data=\n",data.glom().collect())
    print ("result=\n",result.glom().collect())
# //MAPPARTITIONSWITHINDEX
# println("MAPPARTITIONSWITHINDEX")
# val x= sc.parallelize(Array(1,2,3), 2)
# def f(partitionIndex:Int, i:Iterator[Int]) = {
# (partitionIndex, i.sum).productIterator
# }
# val y= x.mapPartitionsWithIndex(f)
# // glom() flattens elements on the same partition
# val xOut= x.glom().collect()
# val yOut= y.glom().collect()
# println(x)
# println(xOut)
# println(yOut)
# //x:Array(Array(1), Array(2, 3))
# //y:Array(Array(0, 1), Array(1, 5))
def f(index, intarray):
    return (index, sum(intarray))
    
def mappartitions_with_index():
    config = SparkConf().setAppName("mappingPartitionsWithIndex")
    sc = SparkContext(conf=config)
    old_data = [1,2,3]
    data = sc.parallelize(old_data,2)
    print ("data=\n", data.glom().collect())
    result= data.mapPartitionsWithIndex(f)
    print ("mappingPartitionsWithIndex=\n", result.glom().collect())

# //SAMPLE
# println("SAMPLE")
# val x= sc.parallelize(Array(1, 2, 3, 4, 5))
# val y= x.sample(false, 0.4)
# // omitting seed will yield different output
# println(x)
# println(y.collect().mkString(", "))
# //x:[1, 2, 3, 4, 5]
# //y:[1, 3]    
def sample():
    config=SparkConf().setAppName("Sample")
    sc = SparkContext(conf=config)
    old_data = [1,2,3,4,5,6,7,8,9,10]
    data = sc.parallelize(old_data)
    print ("Source=\n", data.collect())
    result = data.sample(False,0.4)
    print ("Sample=\n", ", ".join(str(x) for x in result.collect()))

# //UNION
# println("UNION")
# val x= sc.parallelize(Array(1,2,3), 2)
# val y= sc.parallelize(Array(3,4), 1)
# val z= x.union(y)
# val zOut= z.glom().collect()
# println(x)
# println(y)
# println(zOut)
# //x:[1, 2, 3]
# //y:[3, 4]
# //z:[[1], [2, 3], [3, 4]]    
def union():
    config = SparkConf().setAppName("Union")
    cs = SparkContext(conf=config)
    data1 = cs.parallelize([1,2,3],2)
    print ("union1=\n",data1.glom().collect())
    data2 = cs.parallelize([3,4],1)
    print ("union2=\n",data2.glom().collect())
    result = data1.union(data2)
    print ("union=\n",result.glom().collect())

# //JOIN
# println("JOIN")
# val x= sc.parallelize(Array(("a", 1), ("b", 2)))
# val y= sc.parallelize(Array(("a", 3), ("a", 4), ("b", 5)))
# val z= x.join(y)
# println(x)
# println(y)
# println(z.collect().mkString(", "))
# //x:[("a", 1), ("b", 2)]
# //y:[("a", 3), ("a", 4), ("b", 5)]
# //z:[('a', (1, 3)), ('a', (1, 4)), ('b', (2, 5))]
def join():
    config = SparkConf().setAppName("Join")
    cs = SparkContext(conf=config)
    data1=cs.parallelize([("a",1),("b",2)])
    data2=cs.parallelize([("a",3),("a",4),("b", 5)])
    result = data1.join(data2)
    print ("data1=\n", data1.collect())
    print ("data2=\n", data2.collect())
    print ("result=\n", result.collect())
#x:[("a", 1), ("b", 2)]
#y:[("a", 3), ("a", 4), ("b", 5)]
#z:[('a', (1, 3)), ('a', (1, 4)), ('b', (2, 5))]

# //DISTINCT
# println("DISTINCT")
# val x= sc.parallelize(Array(1,2,3,3,4))
# val y= x.distinct()
# println(x)
# println(y.collect().mkString(", "))
# //x:[1, 2, 3, 3, 4]
# //y:[1, 2, 3, 4]
def distinct():
    config = SparkConf().setAppName("Distinct")
    sc = SparkContext(conf=config)
    data = sc.parallelize([1,2,3,3,4])
    result = data.distinct()
    print ("distinct=\n",result.collect())
#x:[1, 2, 3, 3, 4]
#y:[1, 2, 3, 4]

# //COALESCE
# println("COALESCE")
# val x= sc.parallelize(Array(1, 2, 3, 4, 5), 3)
# val y= x.coalesce(2)
# val xOut= x.glom().collect()
# val yOut= y.glom().collect()
# println(xOut)
# println(yOut)
# //x:[[1], [2, 3], [4, 5]]
# //y:[[1], [2, 3, 4, 5]]
def coalesce():
    config = SparkConf().setAppName("Coalesce")
    sc = SparkContext(conf=config)
    data = sc.parallelize([1,2,3,4,5],3)
    result = data.coalesce(2)
    print ("source=\n", data.glom().collect())
    print ("result=\n", result.glom().collect())
#x:[[1], [2, 3], [4, 5]]
#y:[[1], [2, 3, 4, 5]]

# //KEYBY
# println("KEYBY")
# val x= sc.parallelize(
# Array("John", "Fred", "Anna", "James"))        
# ////cache()
# val y= x.keyBy(w => w.charAt(0))
# println(x)
# println(y.collect().mkString(", "))
# //x:['John', 'Fred', 'Anna', 'James']
# //y:[('J','John'),('F','Fred'),('A','Anna'),('J','James')]
def keyby():
    config = SparkConf().setAppName("Keyby")
    sc = SparkContext(conf=config)
    data=sc.parallelize(["John", "Fred", "Anna", "James"])
    result = data.keyBy(lambda x: x[0])
    print ("source=\n", data.collect())
    print ("result=\n", result.collect())
#x:['John', 'Fred', 'Anna', 'James']
#y:[('J','John'),('F','Fred'),('A','Anna'),('J','James')]

# println("PARTITIONBY")
# import org.apache.spark.Partitioner
# val x= sc.parallelize(Array(('J',"James"),('F',"Fred"),
# ('A',"Anna"),('J',"John")), 3)
# val y= x.partitionBy(new Partitioner() { 
# val numPartitions= 2
# def getPartition(k:Any) = { 
# if (k.asInstanceOf[Char] < 'H') 0 else 1 
# }
# })
# val yOut= y.glom().collect()
#x:Array(Array((A,Anna), (F,Fred)), Array((J,John), (J,James)))
#y:Array(Array((F,Fred), (A,Anna)), Array((J,John), (J,James))) 
def partitionby():
    config = SparkConf().setAppName("partitionby")
    sc = SparkContext(conf=config)
    data = sc.parallelize([('J',"James"),('F',"Fred"),('A',"Anna"),('J',"John")], 3)
    #getPartition function (as partitioner function) will get key as a parameter and will 
    #partition the set by keys: before 'H'-one partition, during and after 'H' - another partition
    def getPartition(key):
        if key<"H":
            return 0
        else:
            return 1
    result = data.partitionBy(2,getPartition)
    print ("PartitionBy",result.glom().collect())


# println("ZIP")
# val x= sc.parallelize(Array(1,2,3))
# val y= x.map(n=>n*n)
# val z= x.zip(y)
# println(x)
# println(y)
# println(z.collect().mkString(", "))

def zip():
    config = SparkConf().setAppName("ZIP")
    sc = SparkContext(conf=config)
    data = sc.parallelize([1,2,3])
    data1 = data.map(lambda x: x*x)
    result = data.zip(data1)
    print ("ZIP=\n", result.collect())
#x:[1, 2, 3]
#y:[1, 4, 9]
#z:[(1, 1), (2, 4), (3, 9)]

####################################################################################################################
#Caching or persistence are optimization techniques for (iterative and interactive) Spark computations. 
#They help saving interim partial results so they can be reused in subsequent stages. 
#These interim results as RDDs are thus kept in memory (default) or more solid storage like disk and/or replicated. 
#RDDs can be cached using cache operation. They can also be persisted using persist operation.
#
#persist, cache
#These functions can be used to adjust the storage level of a RDD. 
#When freeing up memory, Spark will use the storage level identifier to decide which partitions should be kept. 
#The parameter less variants  persist() and cache() are just abbreviations for persist(StorageLevel.MEMORY_ONLY).
#
#Warning: Once the storage level has been changed, it cannot be changed again!
def cache_persist():
    conf = SparkConf().setAppName('MyFirstStandaloneApp8')
    sc = SparkContext(conf=conf) 
    best_story = ["movie1","movie3","movie7","movie5","movie8"]
    words = sc.parallelize(best_story)
    words.cache() 
    caching = words.is_cached 
    print ("Words got cached > %s" % (caching))
    caching = words.persist().is_cached 
    print ("Words got cached > %s" % (caching))
    sc.stop()
###################################################################################################################
def getstoragelevel():
    import pyspark
    sc = SparkContext (
       "local", 
       "storagelevel app"
    )
    rdd1 = sc.parallelize([1,2,3,4,5,6,7,8,9],5)
    rdd1.persist( pyspark.StorageLevel.MEMORY_AND_DISK_2 )
    rdd1.getStorageLevel()
    print ("data=\n",rdd1.glom().collect())
    print ("LEVEL=\n",rdd1.getStorageLevel())
    sc.stop()
#Broadcast variables are pretty simple in concept. They're variables that we want 
#to share throughout our cluster. However there are a couple of caveats that are 
#important to understand. Broadcast variables have to be able to fit in memory on 
#one machine. That means that they definitely should NOT be anything super large, 
#like a large table or massive vector. Secondly, broadcast variables are immutable, 
#meaning that they cannot be changed later on. This may seem inconvenient but it 
#truly suits their use case. If you need something that can change, I'd certainly 
#point you to accumulators.
def broadcast():
    conf = SparkConf().setAppName('MyFirstStandaloneApp9')
    sc = SparkContext("local", "Broadcast app") 
    words_new = sc.broadcast(["scala", "java", "hadoop", "spark", "akka"]) 
    data = words_new.value 
    print ("Stored data:\n %s" % (data) )
    elem = words_new.value[2] 
    print ("Printing a particular element in RDD:\n %s" % (elem))
    sc.stop()    
# Serialization is used for performance tuning on Apache Spark. All data that is sent over the network or written to the disk or persisted in the memory should be serialized. Serialization plays an important role in costly operations.
# PySpark supports custom serializers for performance tuning. The following two serializers are supported by PySpark MarshalSerializer
# Serializes objects using Python's Marshal Serializer. This serializer is faster than PickleSerializer, but supports fewer datatypes.
# class pyspark.MarshalSerializer
# PickleSerializer
# Serializes objects using Python's Pickle Serializer. This serializer supports nearly any Python object, but may not be as fast as more specialized serializers.
# class pyspark.PickleSerializer
#
# Serialization plays an important role in the performance of any distributed application. Formats that are slow to serialize objects into, 
# or consume a large number of bytes, will greatly slow down the computation. Often, this will be the first thing you should tune to 
# optimize a Spark application. The Java default serializer has very mediocre performance regarding runtime as well as the size of its results. 
# Therefore the Spark team recommends to use the Kryo serializer instead.
# The following code shows an example of how you can turn on Kryo and how you can register the classes that you will be serializing:
#  val conf = new SparkConf().setAppName(...).setMaster(...)
#       .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
#       .set("spark.kryoserializer.buffer.max", "128m")
#       .set("spark.kryoserializer.buffer", "64m")
#       .registerKryoClasses(
#         Array(classOf[ArrayBuffer[String]], classOf[ListBuffer[String]])
#       )
def serializer():
    #Serializer for RDD
    from pyspark.serializers import MarshalSerializer
    sc = SparkContext("local", "serialization app", serializer = MarshalSerializer())
    print(sc.parallelize(list(range(1000))).map(lambda x: 2 * x).take(10))
    sc.stop()    

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
    
def accumulator():
    global Over_age, Under_age 
    conf = SparkConf().setAppName('MyFirstStandaloneApp10').setMaster("local")
    sc = SparkContext(conf=conf)
    userRDD = sc.textFile("C:\\Users\\AlexR\\PycharmProjects\\pythonProject\\pyspark\\user.txt",1).cache()
    data_with_age_bucket = userRDD.map(parse_N_calculate_age)   
    Under_age = sc.accumulator(0)
    Over_age = sc.accumulator(0)
    df = data_with_age_bucket.map(outliers).collect()
    print ("data=\n", df)
    print ("Under age users of the movie are ",Under_age)
    print ("Over age users of the movie are ",Over_age)
    sc.stop()
    
def intersection():    
    conf = SparkConf().setAppName('MyFirstStandaloneApp6')
    sc = SparkContext(conf=conf) 
    Cricket_team = ["sachin","abhay","michael","rahane","david","ross","raj","rahul","hussy","steven","sourav"]
    Toppers = ["rahul","abhay","laxman","bill","steve"]
    cricketRDD = sc.parallelize(Cricket_team)
    toppersRDD = sc.parallelize(Toppers)
    toppercricketers = cricketRDD.intersection(toppersRDD)
    print ("result=\n", toppercricketers.collect())
    sc.stop()

#ACTIONS
# //GETNUMPARTITION
# println("GETNUMPARTITION")
# val x= sc.parallelize(Array(1,2,3), 2)
# val y= x.partitions.size
# val xOut= x.glom().collect()
# println(x)
# println(y)

def getnumpartititon():
    config = SparkConf().setAppName("getnumpartition")
    sc = SparkContext(conf=config)
    data = sc.parallelize([1,2,3],2)
    result = data.getNumPartitions()
    print ("x=\n", data.glom().collect())
    print ("num. partitions=\n",result)
# //x:[[1], [2, 3]]
# //y:2

# //COLLECT
# println("COLLECT")
# val x= sc.parallelize(Array(1,2,3), 2)
# val y= x.collect()
# val xOut= x.glom().collect()
# println(x)
# println(y)
def collect():
    config=SparkConf().setAppName("Collect")
    sc=SparkContext(conf=config)
    data = sc.parallelize([1,2,3],2)
    result = data.collect()
    print ("data=\n",data.glom().collect())
    print ("result=\n",result)
# //x:[[1], [2, 3]]
# //y:[1, 2, 3]

# //REDUCE
# println("REDUCE")
# val x= sc.parallelize(Array(1,2,3,4))
# val y= x.reduce((a,b) => a+b)
# println(x.collect.mkString(", "))
# println(x)
# println(y)
def reduce():
    config=SparkConf().setAppName("reduce")
    sc=SparkContext(conf=config)
    data = sc.parallelize([1,2,3,4])
    result=data.reduce(lambda x,y: x+y)
    print ("data=\n",data.collect())
    print ("result=\n",result)
# //x:[1, 2, 3, 4]
# //y:10

# //AGGREGATE
# println("AGGREGATE")
# //Aggregate all the elements of the RDD by: 
# //-applying a user function to combine elements with user-//supplied objects, 
# //-then combining those user-defined results via a second //user function, 
# //-and finally returning a result to the driver.
# def seqOp= (data:(Array[Int], Int), item:Int) => (data._1 :+ item, data._2 + item)
# def combOp= (d1:(Array[Int], Int), d2:(Array[Int], Int)) => (d1._1.union(d2._1), d1._2 + d2._2)
# val x= sc.parallelize(Array(1,2,3,4))
# val y= x.aggregate((Array[Int](), 0))(seqOp, combOp)
# println(x)
# println(y)
#lambda x,y:x[0].append(y),x[1]+y
#def f1((array,i),counter):
def f1(a , counter):
    print(counter)
    array = a[0]
    i = a[1]
    array.append(counter)
    i=i+counter
    return (array,i)
#lambda d1,d2: d1[0].extend(d2[0]), d1[1]+d2[1]
def f2(d1,d2):
    print("d1=",d1)
    print("d2=",d2)
    d1[0].extend(d2[0])
    dd=d1[1]+d2[1]
    return (d1[0],dd)
def aggregate():
    config=SparkConf().setAppName("aggregate")
    sc=SparkContext(conf=config)
    data=sc.parallelize([1,2,3,4])
    result=data.aggregate(([],0),f1,f2)
    print ("data=\n",data.collect())
    print ("result=\n",result)
# //x:[1, 2, 3, 4]
# //y:(Array(3, 1, 2, 4),10)
"""
1
4
3
2
d1= ([], 0)
d2= ([1], 1)
d1= ([1], 1)
d2= ([2], 2)
d1= ([1, 2], 3)
d2= ([3], 3)
d1= ([1, 2, 3], 6)
d2= ([4], 4)
data=
 [1, 2, 3, 4]
result=
 ([1, 2, 3, 4], 10)
"""

# //MAX
# println("MAX")
# val x= sc.parallelize(Array(2,4,1))
# val y= x.max
# println(x.collect().mkString(", "))
# println(x)
# println(y)
# //x:[2, 4, 1]
# //y:4
def fmax():
    config=SparkConf().setAppName("Max")
    sc = SparkContext(conf=config)
    data=sc.parallelize([2,4,1])
    result = data.max()
    print ("max=\n",result)
# //SUM
# println("SUM")
# val x= sc.parallelize(Array(2,4,1))
# val y= x.sum
# println(x.collect().mkString(", "))
# println(x)
# println(y)
def fsum():
    config=SparkConf().setAppName("Sum")
    sc = SparkContext(conf=config)
    data=sc.parallelize([2,4,1])
    result = data.sum()
    print ("sum=\n",result)
# //x:[2, 4, 1]
# //y:7
# 
# //MEAN
# println("MEAN")
# val x= sc.parallelize(Array(2,4,1))
# val y= x.mean
# println(x.collect().mkString(", "))
# println(x)
# println(y)
def fmean():
    config=SparkConf().setAppName("Mean")
    sc = SparkContext(conf=config)
    data=sc.parallelize([2,4,1])
    result = data.mean()
    print ("mean=\n",result)
# //x:[2, 4, 1]
# //y:2.3333333
# 
# //STDEV
# println("STDEV")
# val x= sc.parallelize(Array(2,4,1))
# val y= x.stdev
# println(x.collect().mkString(", "))
# println(x)
# println(y)
def fstdev():
    config=SparkConf().setAppName("Stdev")
    sc = SparkContext(conf=config)
    data=sc.parallelize([2,4,1])
    result = data.stdev()
    print ("stdev=\n",result)
# //x:[2, 4, 1]
# //y:1.2472191
# 
# //COUNTBYKEY
# println("COUNTBYKEY")
# val x= sc.parallelize(Array(('J',"James"),('F',"Fred"),
# ('A',"Anna"),('J',"John")))
# val y= x.countByKey()
# println(x)
# println(y)
def countbykey():
    config=SparkConf().setAppName("CountByKey")
    sc = SparkContext(conf=config)
    data = sc.parallelize([('J',"James"),('F',"Fred"), ('A',"Anna"),('J',"John")])
    result = data.countByKey()
    print ("data=\n",data.collect())
    print ("result=",dict(result))
    print ("J=",result["J"])
# //x:[('J', 'James'), ('F','Fred'),('A','Anna'), ('J','John')]
# //y:{'A': 1, 'J': 2, 'F': 1}

# data=[('1', '20-30', 'M', 'technician', '85711', 24), ('2', '50-60', 'F', 'other', '94043', 53), ('3', '20-30', 'M', 'writer', '32067', 23), ('4', '20-30', 'M', 'technician', '43537', 24), ('5', '30-40', 'F', 'other', '15213', 33), ('6', '40-50', 'M', 'executive', '98101', 42), ('7', '50-60', 'M', 'administrator', '91344', 57), ('8', '30-40', 'M', 'administrator', '05201', 36), ('9', '20-30', 'M', 'student', '01002', 29), ('10', '70-80', 'M', 'student', '01002', 75), ('11', '0-10', 'M', 'student', '01002', 5)]
# RDD_20_30=[('1', '20-30', 'M', 'technician', '85711', 24), ('3', '20-30', 'M', 'writer', '32067', 23), ('4', '20-30', 'M', 'technician', '43537', 24), ('9', '20-30', 'M', 'student', '01002', 29)]
# aaaaaa  ('1', '20-30', 'M', 'technician', '85711', 24)
# bbbbbb  technician
# aaaaaa  ('3', '20-30', 'M', 'writer', '32067', 23)
# bbbbbb  writer
# aaaaaa  ('4', '20-30', 'M', 'technician', '43537', 24)
# bbbbbb  technician
# aaaaaa  ('9', '20-30', 'M', 'student', '01002', 29)
# bbbbbb  student
# Total user count is  11
# Total user filtered count is  4
# Total movie users profession wise  {'technician': 2, 'writer': 1, 'student': 1}
# TOTAL len  3
#lambda x:x[3]
def proc(line):
    print ("aaaaaa ",line)
    print ("bbbbbb ",line[3])
    return line[3]
def parse_N_calculate_age2(data):
    (userid,age,gender,occupation,zip) = data.split("|")
    return  userid, age_group2(int(age)),gender,occupation,zip,int(age)

def  age_group2(age):
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

#Seems like select a, count(s) from data group by a: collect "keys" and count them, also countByKey, reduceByKey...
def count_by_value():
    global Over_age, Under_age 
    conf = SparkConf().setAppName('MyFirstStandaloneApp10') #.setMaster("local")
    sc = SparkContext(conf=conf)
    userRDD = sc.textFile("C:\\Users\\AlexR\\PycharmProjects\\PySpark\\PySpark\\user.txt",1) #.cache()
    data = userRDD.map(parse_N_calculate_age)
    print ("data=\n",data.collect())
    RDD_20_30 = data.filter(lambda line : '20-30' in line)
    print ("RDD_20_30=\n",RDD_20_30.collect())
    freq = RDD_20_30.map(proc).countByValue()
    print ("Total user count is ",userRDD.count())
    print ("Total user filtered count is ",RDD_20_30.count())
    print ("Total movie users profession wise ",dict(freq))
    print ("TOTAL len ",len(dict(freq)))
    sc.stop()
    
#add file to every node
# sc addFile
#find path to a file
# SparkFiles.get(filename)
def sparkfiles_addfiles():
    finddistance = "recommend.py"
    path=""
    finddistancename = "finddistance.R"
    sc = SparkContext("local", "SparkFile App")
    sc.addFile(path,finddistance)
    print ("Absolute Path -> %s" % SparkFiles.get(finddistancename))
    sc.stop()

if __name__ == '__main__':
    pass
    #TRANSFORMATION
    #map()
    #filter()
    flatmap()
    #groupby()
    #groupby_countword()
    #groupbykey()
    #reducebykey_vs_groupbykey()
    #mappartitions()
    #mappartitions_with_index()
    #sample()
    #union()
    #join()
    #distinct()
    #coalesce()
    #keyby()
    #partitionby()
    #zip()
    #cache_persist()
    #getstoragelevel()
    #broadcast()
    #intersection()
    
    #ACTIONS
    #getnumpartititon()
    #collect()
    #reduce()
    #aggregate()
    #fmax()
    #fmean()
    #fstdev()
    #countbykey()
    #count_by_value()
    #accumulator()
    #sparkfiles_addfiles()