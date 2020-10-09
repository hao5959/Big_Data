# SPARK
##### Structure
```
   SparkSQL  	    SparkStreaming		Mlib		GraphX
structured data      realtime cal
          \             |                /          /
			APACHE SPARK (spark core)
```
```
Submit task to client  
SparkSubmit()  		-----> Cluster Manager -----> WORKER executor (run spark task)  
Driver  
```
##### RDD
- Resilient
  - 容错
  - 可以缓存在内存和磁盘, 或外部存储
- Distributed
  - 支持分区
- Datasets

```
1. List or Set of partitions  
2. A function for computing each split
3. List of dependencies on other (parent) RDD
4. RDD is an immutable, partitioned collection of elements on the cluster which can be operated in parallel
5. Fault Tolerant
// 保存RDD之间的依赖关系
// checkpoint 直接将RDD的数据存放在外部存储系统, 出现问题直接读取
- properties
    A list of partitions
    A function for computing each split
    A list of dependencies on other RDDs
    Optionally, a Partitoner for key-value RDDs(e.g. to say that the RDD is hash-partitioned)
    Optionally, a list of preferred locations to compute each split on(e.g. block locations for an HDFS file)
```

use Spark API to create RDD  
Spark Core entry point: SC

```
Transformation  转换操作 惰性操作 map, flatMap, filter...
Action  动作操作 reduce, collect...
```

```scala
// 1. 通过本地集合  \  
// 2. 通过外部数据  ----> To create RDD  
// 3. 通过RDD衍生  /  
// 1
def rddCreationLocal(): Unit = {
    val seq = Seq("hello1", "hello2", "hello3")
    val rdd1: RDD[String] = sc.parallelize(seq, numSlices=2)//可以没有numSlices
    val rdd2: RDD[String] = sc.makeRDD(seq, numSlices=2)
}
// 2
def rddCreationExternal(): Unit = {
    sc.textFile(path=" ... ")
// textFile 传入的是什么？ path
// 是否支持分区？ 如果path="hdfs:/// ..." 分区是HDFS中block决定的
// 也支持cloud
}
// 3
def rddCreateFromRdd(): Unit = {
	val rdd1 = sc.parallelize(Seq(1, 2, 3))
    val rdd2 = rdd1.map(item => item)
// RDD is immutable
}
```
```scala
// create spark context
// first create spark conf, this is used to packaged some parameters

val conf = new SparkConf().setMaster("local[6]").setAppName("appName")
val sc = new SparkContext(conf)
// SparkContext can be used to create RDD, set parameter, set jar package...
sc.api

// close SparkContext to release cluster resources
sc.stop()
```
##### Map, FlatMap, reduceByKey
```scala
// Create RDD
// Create Map
// Collect Result
```

```
Quick: memory computing  
Lazy Evalution: optimize execution plan, return action when you want to get the result  
```
```
Logical Optimization: Lazy Evaluation and DAG
```
- Spark application: Driver & Executors
```
Driver:
- Maintaining information about the spark application during the lifetime of the app
- Responding to a user's program or input 
- Analyzing, distributing, and scheduling work across the executors
Executors:
- Do the work that the driver assigns to them
- Static/ Dynamic allocation
```
#### Spark Key Concepts
- SparkSession
```
entry point to programming spark with dataset and dataframe API
spark -> sparkSession -> functions
```
- DataSet 
```
Strongly typed collection of domain-specific objects that can be transformed in parallel using functional or relational operations (only available to Java/Scala)
check type at compile time
```
- DataFrame
```scala
/* Represents a table of data with rows and columns, 
   not a strong type 
   Spark checks whether data conforms to the data type specified in schema at runtime*/
Type DataFrame = Dataset[Row] // Datasets containing Row Obj
```
- DateFrame Partitions
```
spark break data into chunks (big dataset to small datasets)
represent how data is physically distributed across the cluster of machines during execution
```
```
spark application essentiaally is to apply operations to Partitions
```

- 2 kinds of API/ Operations
```
- Transformations: 
    allow us to build up execution plan
    - Lazy Evaluation
        - predicate pushdown
        - spark compile a execution paln from raw transformations and optimize the pipeline, improve efficiency
    - Two types:
        - Narrow: 1 partition -> 1 partition
        - Wide dependencies: data shuffling too much; will create new stage
- Actions:
    trigger the computation
    - View data in the console
    - Collect data to native object in the repective language
    - Write to output data source
```

```scala 
//catalog  operations related to metadata
spark.conf.getAll
val path = "/data/spark/flight-data/json/2010-summary.json"
val df = spark.read.format("json").load(path)
df.show(5, false)
```

#### Structured API
- Schema
```
A schema defines the column names and types of a DataFrame
    schema-on-read(Parquet, AVRO, infer from JSON, CVS)
    Explicitly define it(Create a StructType object)
        StructType: a list of StructField
        StructField: name, type, nullable
```
```scala
dataframe.take(n: Int)/ takeAsList()
dataframe.first
```
- DataFrame Transformation 
```
3 common ways to create a DataFrame
    from file
    from table
    take a set of rows to convert them to a dataframe

    spark.catalog 
    // meatadata in catalog 
    // stastistic generate catalog
    // analyze table table_name [partition(par_cols)] compute statistic [noscan] 
    Hive and Spark :point_up:
    Impala: compute stats

    withColumn // add column
    sample true: 放回 false: 不放回
```

- Spark Data Sources
```
read: DataFrameReader
readStream: DataStreamReader

DataFrameReader is accessible from SparkSession.
After we have a DataFrame reader, specify: format, schema, A series of options
spark.read.format().option().option().schema().load()

- write data
DataFrameWirter
def wirteStream: DataStreamWriter
accessible from DataFrame
df.write.format().option().option().partitonBy().bucketBy().sortBy().save()
```





[ :point_up: ](#Hadoop) TOP