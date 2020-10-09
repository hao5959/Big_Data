## Sqoop

```
is a tool for efficiently transferring bulk data between Hadoop and RDBs.
```

```
sqoop list-databases \
--connect jdbc:mysql://database.ascendingdc.com:3306/ \
--username xxx \
--password xxx
```

```
sqoop import \
-m 1 \
--connect xxx/retail_db \
-U \
--password \
--compression-codec=snappy \
--as-avrodatafile( or as-parquetfile) \
--table orders \
--fields-terminated-by '|' \
--target-dir sqoopimport/orders

--columns ""
--where ""
```
- data skew
