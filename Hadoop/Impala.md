## IMPALA

- Architecture
```
A mordern MPP(massively parallel processing) SQL Query Engine for the Hadoop Environment
Low latency and high concurrency
IMPALA Design for interactive BI/Analytic Query
HIVE for ETL
No fault tolerance

    StateStore                      CatalogService
                                    /           \
            Hadoop Namenode(file info)      Hive Metastore(table info)
Impalad: impala deamon(calculation) * n
Hadoop Datanode
```

- Catalog Service
```
Impala Metadata publish-subscribe service, broadcast metadata to all impalad

Mediator between Hive's Metastore/ HDFS NameNode and Impala
Executes DDL operations on behalf of Impala Daemons
Serves metadata to Impala Daemons via the statestore broadcast mechanism

DDL
    catalogd will return updated table obj directly to the issuing impalad
    all other impalad will get the updated obj via statestore
If Catalog service died, then cannot make ddl operation
```
- StateStore Service
```
Impala's central state service
    metadata and membership

Impala's metadata publish-subscribe service, which braodcast metadata to all impala daemons
    catalog service will updates to statestore service
    statestore service periodically push updates to all impala daemons. 
    (msg types: topic update; keepalive)
```
- Daemon
```
all impala daemon are symmetric
- Query Planner 
- Query Coordinator
- Query Executor

Each Daemon has a catalog cache to caches metadata
    table schema, hdfs file/ block locations, table stats

```
- *Question*:
```
Chose the right storage engine? Criterons
depends on access pattern
HDFS: scan access pattern
HBase: random access pattern
KUDU: good on both
```
- Performance Tuning
```
choosing the best physical representation for your logical data model
    partitioning
    sorting
    data types
    nested types
Operational optimizations:
    computing statistics
        # of rows, # of data files, total size of data files, min/max value of each column....
        join strategy: shuffle vs broadcast 
        memory estimation
    admission control and memory management 
    impala has compute stats query
```
- Denormalization
```
distribute system hope there is as less join as possible. donot care redundant 
```
- Multitenant Cluster Architecture
```
Security & Governance
    HDFS Information Architecture(IA)
    Authentication
    Authorization
    Auditing
    Quata management
Resource Isolation & Management
- Dividing up finite cluster resource to ensure predictable behavior 
    Static partitioning
    Dynamic partitioning
```
- Impala Admission Control
```
Impala resource management
```
- Impala Mission Control
- Resource Pool
```
memory + cpu
using weight 
```
- Placement Rule
- Scheduling Rule

- Hands on
```
explain query
compute/ drop stats
summary: for last query
    compare avg time and max time (data skew)
    check bottleneck
```