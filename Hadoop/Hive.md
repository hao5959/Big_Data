## HIVE

```
big data is schema on read  
Hive:
    A data warehouse tool built on top of Hadoop
        Hadoop provides storage/Computing Engine
        Complie SQL Queries as MapReduce jobs and run the jobs in the cluster
        Schema info is stored in a RDBMS
        ETL, OLAP
    Data Warehouse
        A database specific for analysis and reporting purposes
```

- Hive Architecture
```
________________________________
|           HiveServer2        |
|------------------------------|
|    Driver          Driver    |      \
|    Executor        Executor  |       Hadoop
|    Complier        Complier  |         |
|                              |        HDFS
|    Session1        Session2  |      /
|                              |
|           MetaStore          |
--------------------------------

Hive metadata stores in an external relational database
* HiveServer2: 
|       \       \
Beeline  JDBC   ODBC ...
    Enables clients to execute queries against Hive;
    Communicate with client by Thrift protocol. Thrift is an RPC framework for building \ 
    cross-platform/multi-language service;
    Parse/Compile Hive query, prepares physical execution plans for various execution \
    engines(MR/Spark/Tez) and submits jobs to the Hadoop cluster for execution.
    query -> hiveserver2 -> logical execution plan -> physical execiton plan
```

- Hive Service 
```
- Compilier
- * Metatore
    Stores Database/Table/Partition properties(schema, SerDe library, table location)
    Table Statistics
        Number of rows/files
        Size in Bytes
        Analyze table <table name> compute statistics/ for columns...
    Metadata stored in external RDBMS
- HCatalog
```

- Hive QL
- Hive Tables Types
```
Managed Table
    Both data and metadata are managed by HIVE
    If a managed table or partition is dropped, the data and metadata associated with that table or partition are deleted
    A managed table is stored in *databasename.db/tablename/folder* under the folder defined by 'hive.metastore.warehouse.dir'
External Table
    An external table describes the schema on external files
    Only table metadata are managed by HIVE
    If an external table or partition is dropped, only the metadata is deleted

HIVE table -> HDFS folder (give the file a schema)
```

