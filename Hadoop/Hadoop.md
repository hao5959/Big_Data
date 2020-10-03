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
```
- HDFS Architecture
```
Client ------> NameNode (metadata)  
            /    |  (heart beat)  
        /        |
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
Pipeline established and the data is written into multiple data nodes (client writes block to the first datanode, first datanode forward data to next in the pipeline)
Close file upon finish
```
<h4 style="color: rgb(35, 205, 182);">SPOF</h4>

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
[ :point_up: ](#Hadoop)
