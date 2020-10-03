# SPARK

##### DAG

##### Structure

```markdown
   SparkSQL  	    SparkStreaming		Mlib		GraphX
structured data      realtime cal
          \             |              /          /
				APACHE SPARK (spark core)
```
```
Submit task to client  
SparkSubmit()  		-----> Cluster Manager -----> WORKER executor (run spark task)  
Driver  
```
sc: spark core RDD 执行入口  
spark context  

##### RDD

- Resilient
  - 容错
  - 可以缓存在内存和磁盘, 或外部存储
- Distributed
 -支持分区
- Datasets

```markdown
1. RDD是数据集
2. RDD是编程模型
3. RDD dependencies
4. RDD是可以分区的  
5. RDD IS READ ONLY  
6. RDD 是可以容错的  
// 保存RDD之间的依赖关系
// checkpoint 直接将RDD的数据存放在外部存储系统, 出现问题直接读取
```

```scala
属性
partition list
compute function
RDD dependencies
partitoner
preferred location
```

use Spark API to create RDD  
Spark Core entry point: SC

```scala
两类算子
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
##### Partition











