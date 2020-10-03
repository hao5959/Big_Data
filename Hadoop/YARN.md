## YARN
##### Yet ANother Resource Negotiator
```
No pre-defined slots
    resources: memory + cpu cores
Support MR and non-MR application running on the same cluster
Most JobTracker functions moved to Application Master
```
- Resource Manager and Node Manager
```
Resource Manger:
    Runs on master node, one per cluster(can have HA, one active, one standby)
    Global resource schduler
    Arbitrates system resources between competing applications
======   
    Manages worker nodes 
        - Track heartbeat from Node Managers
    Manage containers
        - Handle AM requests for resources
        - Recycles container when they expire or the app completes
    Manage Application Masters 
        - Creates a container for running AM and tell the node manager to launch AM
        - Tracks hearbeats from AM
Node Manager:
    Runs on worker nodes, one per worker node
    Run the task on the worker node(Executes any computation that makes sense to Application Master, not only map or reduce task)
    Communicates with Resource Manager
======
    Communicate with Resource Managers
        - Registers and provides info on node resources
        - Send heartbeats and container stauts
    Manage processes in containers
        - Launch AMs on request from RM
        - Launch application processes on request from AM
        - Monitors resources usage by containers; kills run-away processes
    Provides logging services to applications
        - Aggregates logs for an application and saves them to HDFS
```
- Running Application in YARN
```
Containers
    Create by the RM upon request
    Allocate a certain amount of resources(memory, CPU) on a workernode
    Application run in one or more containers
Application Master
    One per application
    Framework/ application specific 
    Runs in a container 
    Requests more containers to run application tasks
    Short life
```
- Fault Tolerance
```
Node Manager Fail
    If NM stops sending heartbeat to RM, it is removed from list of active nodes 
    Tasks on that node will be trated as failed
    If AM node fails, the application will be trated as failed, RM will relaunch the application
Resource Manager Fail
    Standby RM will become active
    If HA is not configured, no applications or tasks can be launched(SPOF)
```
- YARN resource pool
```
Resource Pools 
    Pool is a combination of Memory and CPU resources
    Cluster is shared by multi-tenancy
    Cluster resources is divided into pools
    Associate with scheduling rules, scheduling policy, access control
Scheduling Rules
    Can define different scheduling rules(e.g. weekday and weekend)
    Apply to Resource Pools configuration
Placement Rules
    Determines in which pool an application will run
User Limits
    Defines the Max Running Apps for user
```


[ :point_up: ](#Hadoop) TOP
