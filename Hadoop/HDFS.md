# Hadoop
HDFS, YARN, MapReduce

## HDFS  
- Design Goals
```
- Very Large Distributed File System
- Assumes Commodity Hardware
    Commodity Hardware, failure is normal
    Files are replicated to handle hardware failure
    Detect failures and recover from them
- Optimized for Batch Processing  
Good for:
1. very large files 
2. Streaming data access(scan, read all data), batch processing
3. Write once, read multiple times scenario
Not Good for:
1. Lots of small files
2. Low-latency, random data access
3. File modification at arbitrary offsets. Append-only
```
- HDFS Architecture
```
Client ------> NameNode:active (metadata)  NameNode:standby 
            /    |  (heart beat)         \
        /        |                      JournalNode JournalNodes...
   DataNode    DataNode

Read:
Client open a file in HDFS
Get block locations from Namenode
Based on locations info, determine the datanode where the data block locates
Read data from data node(namenode not engaged in read)
Close file

Write:
Client call create
DFS call create to create a new file in HDFS namespace, DFS returns an FSDataOutputStream object
Client write data into FSDataOutputStream
Pipeline established and the data is written into multiple data nodes 
(client writes block to the first datanode, first datanode forward data to next in the pipeline)
Close file upon finish
```
- SPOF   
```
solution: **High Availablility(HA)**
Use ZooKeeper to ensure that only one Namenode is active
Use Journal Nodes to records HDFS edits, and synchronize active and standby Namenode
    Active Namenode writes edits to JNs
    Standby Namenode reads edits from JNs
```

- Blocks
```
HDFS stores data in Blocks, 128Mb as default
Files in HDFS broken into block-sized chunks, which are stored as independent units
Multiple copies of block(default 3) are stored in different nodes that provide Redundency
```
- NameNode
```
Manage File System Namespace
    Maintains the filesystem tree and the metadata for all the files and directories in the tree  
    Maps a file name to a set of blocks
    Maps a block to the DataNodes where it resides
    Metadata is persisted in local disks called FsImage
Replication Engine for Blocks
```
```
NameNode Metadata
Metadata in Memory 
    The entire metadata is loaded into memory when NameNode starts
Types of metadata
    List of files
    List of Blocks for each file
    List of DataNodes for each block
    File attributes, e.g. creation time, replication factor
A Transaction Log
    Records file creations, file deletions etc
```
- DataNode
```
A Block Server
    Stores data in the local file system
    Stores metadata of a block(e.g. CRC)
    Serves data and metadata to Clients
Block Report
    Periodically sends a report of all existing blocks to the NameNode
Facilitates Pipelining of Data
    Forwards data to other specified DataNodes
```
- HDFS Fault Tolerance
```
Data Replication
Block Placement Policy/ Rack Awareness
    First replica on local node/ rack
    Second replica on a remote rack
    Third replica on same remote rack
    Additional replicas are randomly placed
    Clients read for nested replicas
Heart Beat
    Datanodes send heartbeat to the Namenode
Safe Mode
    When Namenode starts, it enter safe mode 
    No write is allow during safe mode
    In safe mode, Namenode collect heartbeat from Datanode
    When minimum relication of data block is detected, the data block is conside safe
    When certain percentage data blocks become safe, Namenode will exit safe mode after cetain amount of time
    New replicas will be made if necessary
Checksum: Data Correctness
    Use Checksums to validate data(CRC32)
Metadata Protection
HDFS Snapshot
    Point-in-time copies of the file system
    Mark every block, if a block is modified, make a copy of that block
    Commonly used for:
        Data backup
        Protection against user error
        Protection against disaster recovery
```
- HDFS Rebalancer 
```
HDFS works best when the data blocks are evenly spread of across the cluster
Goal: % of disk full on Datanodes should be similar
```
- Secondary Namenode  
```
Is not even a namenode
Copies FsImage and Transaction Log from Namenode to a temporary directory
Merges FsImage and Transaction Log into a new FsImage in temporary directory
Uploads new FsImage to the Namenode, Transaction Log on Namenode is purged
```
- Typical File Formats
```
Parquet, ORC is popular (columnar)
Row VS Column Store
```

[ :point_up: ](#Hadoop) TOP
