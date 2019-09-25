# Hadoop体系生态学习

## Hadoop应用背景

数据的量随着技术的发展急剧增长，原来的单机尺度的数据分析时不能满足要求。<br>

Hadoop就是为了处理这种超过单机尺度的数据<br>

Hadoop及其生态已经事实上成为大数据体系的标准 <br>

## Hadoop的基本构成

### HDFS
HDFS是一种分布式文件系统，是数据存储的物理载体，在它的上层有Hbase、Hive等应用。<br>

### MapReduce
MapReduce，以下简称MR。负责计算数据，但是MR本身计算效率较低。在此基础上发展出了Tez和Spark，是第二代计算引擎。<br>

### YARN
Hadoop的资源监控与调度系统，替代原有的JobTracker。是Hadoop2.0新增的任务框架

## Hadoop生态中的工具、组件

### 数据库

Hive

Hbase

#### 和传统数据库的类比关系 

Hive 好比是分布式版的MySQL <br>
MapReduce、Spark 可以看做是InnoDB引擎[不完全准确] <br>
Hbase 好比是分布式版的MongoDB <br>

#### 应用的场景

HIVE 数据仓库 支持查询和插入，一般用用于企业级的数据分析（OLAP）<br> 
Hbase Key-Value模式，通常需要和redis这样的数据库搭配使用，Hbase用于数据的持久化，Redis作为缓存层，作为数据的直接提供者 <br>


### 计算引擎
#### Spark：
Spark是一个开源集群运算框架，相对于Hadoop的MapReduce会在运行完工作后将中介数据存放到磁盘中，Spark使用了存储器内运算技术，能在数据尚未写入硬盘时即在存储器内分析运算。<br>
Spark在存储器内运行程序的运算速度能做到比Hadoop MapReduce的运算速度快上100倍，即便是运行程序于硬盘时，Spark也能快上10倍速度。<br>
[维基百科](https://zh.wikipedia.org/wiki/Apache_Spark "维基百科"). 
#### Tez：
Tez 产生的主要原因是绕开 MapReduce 所施加的限制。Tez 项目的目标是支持高度定制化，这样它就能够满足各种用例的需要，让人们不必借助其他的外部方式就能完成自己的工作。

#### Spark VS TeX
Spark更像是一个通用的计算引擎，提供内存计算，实时流处理，机器学习等多种计算方式，适合迭代计算
Tez作为一个框架工具，特定为hive和pig提供批量计算

#### Kylin
Kylin和Hive功能是类似的，提供Hadoop/Spark之上的SQL查询接口及多维分析（OLAP）能力以支持超大规模数据。<br>
通过构建一个数据立方体模型，来实现数据的快速查询和相应,理论上能获得比Hive更好的性能 <br>

### ETL


Pig：
Sqoop：
Mahout：
ZooKeeper：
Avro：
Flume：
Pig：
Kafka：
Impala：


#### 参考资料
