## 1. Employee Dataset 

In HDFS /data/spark/employee, there are 4 files:

- dept.txt
- dept-with-header.txt
- emp.txt
- emp-with-header.txt  

Answer following questions by:
1. Spark SQL 
2. Spark DataFrame API

Questions:  
1. List total salary for each dept.
2. List total number of employee and average salary for each dept.
3. List the first hired employee's name for each dept. 
4. List total employee salary for each city.
5. List employee's name and salary whose salary is higher than their manager.
6. List employee's name and salary whose salary is higher than average salary of whole company.
7. List employee's name and dept name whose name start with "J".
8. List 3 employee's name and salary with highest salary.
9. Sort employee by total income (salary + commission), list name and total income.

## 2. Refer to week 03 hive homework, implement all queries by Spark DataFrame API
```
+-----+------+---------+----+----------+----+----+------+-------+----------+-------+
|EMPNO|  NAME|      JOB| MGR|  HIREDATE| SAL|COMM|DEPTNO|DEPT_NO| DEPT_NAME|    LOC|
+-----+------+---------+----+----------+----+----+------+-------+----------+-------+
| 7369| SMITH|    CLERK|7902|1980-12-17| 800|   0|    20|     20|  RESEARCH| DALLAS|
| 7499| ALLEN| SALESMAN|7698|1981-02-20|1600| 300|    30|     30|     SALES|CHICAGO|
| 7521|  WARD| SALESMAN|7698|1981-02-22|1250| 500|    30|     30|     SALES|CHICAGO|
| 7566| JONES|  MANAGER|7839|1981-04-02|2975|   0|    20|     20|  RESEARCH| DALLAS|
| 7654|MARTIN| SALESMAN|7698|1981-09-28|1250|1400|    30|     30|     SALES|CHICAGO|
| 7698| BLAKE|  MANAGER|7839|1981-05-01|2850|   0|    30|     30|     SALES|CHICAGO|
| 7782| CLARK|  MANAGER|7839|1981-06-09|2450|   0|    10|     10|ACCOUNTING|NEW YOR|
| 7839|  KING|PRESIDENT|null|1981-11-17|5000|   0|    10|     10|ACCOUNTING|NEW YOR|
| 7844|TURNER| SALESMAN|7698|1981-09-08|1500|   0|    30|     30|     SALES|CHICAGO|
| 7900| JAMES|    CLERK|7698|1981-12-03| 950|   0|    30|     30|     SALES|CHICAGO|
| 7902|  FORD|  ANALYST|7566|1981-12-03|3000|   0|    20|     20|  RESEARCH| DALLAS|
| 7934|MILLER|    CLERK|7782|1982-01-23|1300|   0|    10|     10|ACCOUNTING|NEW YOR|
+-----+------+---------+----+----------+----+----+------+-------+----------+-------+
```
```scala
// 1
import org.apache.spark.sql.types._
val empSchema = new StructType(
	Array(
        new StructField("EMPNO", LongType, true),
        new StructField("NAME", StringType, true),
        new StructField("JOB", StringType, true),
        new StructField("MGR", StringType, true),
        new StructField("HIREDATE", DateType, true),
        new StructField("SAL", LongType, true),
        new StructField("COMM", LongType, true),
        new StructField("DEPTNO", LongType, true)
      )) 
val path_emp = "/data/spark/employee/emp-with-header.txt"
val emp = spark.read.format("csv").option("header", true).schema(empSchema).load(path_emp)
emp.show(false)
emp.groupBy("DEPTNO").sum("SAL").show(false)

val dept = spark.read.format("csv").option("header", true).option("inferSchema", true).load(path_dept)
val joinExpr = emp.col("DEPTNO") === dept.col("DEPT_NO")
import org.apache.spark.sql.functions._
emp.join(dept, joinExpr).groupBy("DEPT_NAME").agg(sum("SAL").alias("sum_sal")).show
有时间再加一个sort

+----------+-------+
| DEPT_NAME|sum_sal|
+----------+-------+
|  RESEARCH|   6775|
|ACCOUNTING|   8750|
|     SALES|   9400|
+----------+-------+
```
```scala
// 2
emp.join(dept, joinExpr).groupBy("DEPT_NAME").agg(count("NAME").as("emp_count"), avg("SAL").as("avg_sal")).show
+----------+---------+------------------+                                       
| DEPT_NAME|emp_count|           avg_sal|
+----------+---------+------------------+
|  RESEARCH|        3|2258.3333333333335|
|ACCOUNTING|        3|2916.6666666666665|
|     SALES|        6|1566.6666666666667|
+----------+---------+------------------+
看一下avg能不能round
```
```scala
// 3
emp.join(dept, joinExpr).groupBy("DEPT_NAME").agg(first("NAME"), min("HIREDATE").as("earilest")).show
+----------+------------------+----------+                                      
| DEPT_NAME|first(NAME, false)|  earilest|
+----------+------------------+----------+
|ACCOUNTING|             CLARK|1981-06-09|
|  RESEARCH|             SMITH|1980-12-17|
|     SALES|             ALLEN|1981-02-20|
+----------+------------------+----------+
```
```scala
// 4
emp.join(dept, joinExpr).groupBy("LOC").agg(sum("SAL").as("TOTAL_SAL")).show
+-------+---------+                                                             
|    LOC|TOTAL_SAL|
+-------+---------+
| DALLAS|     6775|
|CHICAGO|     9400|
|NEW YOR|     8750|
+-------+---------+
```
```scala
// 5
val joinExpression = emp.col("EMPNO") === emp1.col("MGR")
emp.join(emp1, joinExpression).select(emp1("NAME"), emp1("SAL")).where(emp("SAL") < emp1("SAL")).show()
+----+----+
|NAME| SAL|
+----+----+
|FORD|3000|
+----+----+
```
```scala
// 6
val avg_sal = emp.agg(avg("SAL")).collect()(0)(0)
emp.where(col("SAL") > avg_sal).select("NAME", "SAL").show()
+-----+----+
| NAME| SAL|
+-----+----+
|JONES|2975|
|BLAKE|2850|
|CLARK|2450|
| KING|5000|
| FORD|3000|
+-----+----+
```
```scala
// 7
emp.join(dept, joinExpr).where(col("NAME").like("J%")).select("NAME", "DEPT_NAME").show()
+-----+---------+
| NAME|DEPT_NAME|
+-----+---------+
|JONES| RESEARCH|
|JAMES|    SALES|
+-----+---------+
```
```scala
// 8
emp.orderBy(col("SAL").desc).limit(3).select("NAME", "SAL").show()
+-----+----+                                                                    
| NAME| SAL|
+-----+----+
| KING|5000|
| FORD|3000|
|JONES|2975|
+-----+----+
```
```scala
// 9
val emp_9 = emp.withColumn("total_income", col("SAL")+col("COMM"))
emp_9.orderBy(col("total_income").desc).select("NAME", "total_income").show()
+------+------------+                                                           
|  NAME|total_income|
+------+------------+
|  KING|        5000|
|  FORD|        3000|
| JONES|        2975|
| BLAKE|        2850|
|MARTIN|        2650|
| CLARK|        2450|
| ALLEN|        1900|
|  WARD|        1750|
|TURNER|        1500|
|MILLER|        1300|
| JAMES|         950|
| SMITH|         800|
```
- Spark SQL
```scala
// 1
emp.createOrReplaceTempView("empTable")
dept.createOrReplaceTempView("deptTable")
spark.sql("select DEPT_NAME, sum(SAL) from empTable join deptTable on empTable.DEPTNO = deptTable.DEPT_NO group by DEPT_NAME").show

```
```scala
// 2
spark.sql("select DEPT_NAME, count(NAME) as emp_count, round(avg(SAL), 0) as avg_sal from empTable join deptTable on empTable.DEPTNO = deptTable.DEPT_NO group by DEPT_NAME").show
```
```scala
// 3
spark.sql("select DEPT_NAME, NAME, HIREDATE from empTable join deptTable on empTable.DEPTNO = deptTable.DEPT_NO where HIREDATE in (select min(HIREDATE) from empTable group by DEPTNO)").show
```
```scala
// 4
spark.sql("select sum(SAL) as total_sal, LOC from empTable join deptTable on empTable.DEPTNO = deptTable.DEPT_NO group by LOC").show
```
```scala
// 5
spark.sql("select e2.NAME as name, e2.SAL as sal from empTable e1, empTable e2 where e1.EMPNO = e2.MGR and e1.SAL < e2.SAL").show
```
```scala
// 6
spark.sql("select NAME, SAL from empTable where SAL > (select avg(SAL) from empTable)").show
```
```scala
// 7
spark.sql("select dept_name, name from empTable join deptTable on empTable.deptno = deptTable.dept_no where name like 'J%'").show 
```
```scala
// 8
spark.sql("select name, sal from empTable order by sal desc limit 3").show
```
```scala
// 9
spark.sql("select name, sal+comm as total_income from empTable order by total_income desc").show 
```