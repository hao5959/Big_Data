# scala  
val 的引用不可以改
```scala
val arr: Array[Int] = Array(1,2,3,4,5)
for(i <- arr) yield i * 10
arr.map(_ * 10)
arr.map(m => m * 10)
arr.filter(m => m % 2 == 1).map(n => n * 1000)
```
```scala
val i = 1.+(2)  //this is a method
```
#### method
```scala
def sum(x: Int, y: Int): Int = x + y
// sum(1,2)
def +(x: Int, y: Int): Int = {x + y}
// $plus(1,3)
def factorial(x: Int): Int = x * x
```
#### function
```scala
//function can used as an parameter in the method
val f1 = (x: Int, y: Int) => x + y
val f2 :(Int, Int) => Int = {(x, y) => x + y}

val f0 = (x: Int) => x.toDouble
val f1: Int => Double = { x => 1.toDouble }

val f: Int => Int = { x => x * x }
arr.map(f) //Array[Int] = Array(1, 9, 25, 49, 81)
arr.map((x: Int) => x * x)
```
```scala
// `method name` + `_` will transfer method to function
// `factorial` is a method 
// `factorial _` is a function
arr.map(factorial) 
arr.map(factorial _)
arr.map(x => factorial(x))
```
#### Collections
The length of Array is immutable
```scala
import scala.collection.mutable._ (ArrayBuffer, ListBuffer, HashMap...)
val ab = new ArrayBuffer[Int]()
ab += 1
ab -= 1 //fifo
val ab2 = ArrayBuffer(5, 4, 3, 2, 1)
ab += (1, 2, 3, 4)
ab ++= a2
val array = new Array[Int](8)
val array = Array[Int](10)

// arr.sum  arr.max   arr.min  arr.sorted/sortwith/sortBy
// Map
val m = Map("a" -> 1, "b" -> 2)
val m = Map(("a", 1), ("b", 2))
```
```scala
// calculate words count
val words: Array[String] = Array("Hello Scala", "Hello Spark", "Hello Scala", "Hello Scala", "hello World", "Hello Spark")
// val words = Array("Hello Scala", "Hello Spark", "Hello Scala", "Hello Scala", "hello World", "Hello Spark")
words.map(x => x.split(" ")).flatten
words.flatMap(_.split(" ")).map((_, 1)).groupBy(_._1).map(t => (t._1, t._2.length)).toList.sortBy(_._2).reverse
```
```scala
// reduce
arr.reduce(_+_)
arr.fold(100)(_+_)
``` 
#### parallel collections

[ :point_up: ](#Hadoop) TOP