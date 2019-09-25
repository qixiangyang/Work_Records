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

#### Hive
其优点是学习成本低，可以通过Hive是基于Hadoop的一个数据仓库工具，可以将结构化的数据文件映射为一张数据库表，并提供简单的SQL查询功能，可以将SQL语句转换为MapReduce任务进行运行。<br>
类SQL语句快速实现简单的MapReduce统计，不必开发专门的MapReduce应用，十分适合数据仓库的统计分析。<br>
#####  应用场景
用作数据仓库 一般用用于企业级的数据分析（OLAP）<br> 

#### Hbase

HBase是一个开源的非关系型分布式数据库（NoSQL），它可以对稀疏文件提供极高的容错率。<br> 
它参考了谷歌的BigTable建模,运行于HDFS文件系统之上.
##### 应用场景
Hbase 类似于Key-Value模式，写入性能极佳，可扩充性强。并发读取速度快<br>

#### 不同数据库的类比关系 

Hive: 这部分要先实践一下再来写。核心 Hive存储的数据格式

##### Hive VS Hbase

Hbase和Hive在大数据架构中处在不同位置，Hbase主要解决实时数据查询问题，Hive主要解决数据处理和计算问题，一般是配合使用。

##### Hbase MongoDB, Redis
Redis： 作为关系型数据库的缓存层，加速数据访问；同时提供数据落地功能 <br>
MongoDB： schema-less的数据库，在变化快、事务性要求不强的场景，用于替代MySql，比如游戏用户信息、社交信息的存储 <br>
HBase：海量数据的存储，需要高并发查询的场景[简单查询]，比如日志 <br>
参考资料：[Memcached、Redis、MongoDB、HBase对比](https://juejin.im/entry/5b120f016fb9a01e53 28261e "Memcached、Redis、MongoDB、HBase对比").

### 计算引擎
#### Spark：
Spark是一个开源集群运算框架，相对于Hadoop的MapReduce会在运行完工作后将中介数据存放到磁盘中，Spark使用了存储器内运算技术，能在数据尚未写入硬盘时即在存储器内分析运算。<br>
Spark在存储器内运行程序的运算速度能做到比Hadoop MapReduce的运算速度快上100倍，即便是运行程序于硬盘时，Spark也能快上10倍速度。<br>
参考资料：[维基百科](https://zh.wikipedia.org/wiki/Apache_Spark "维基百科"). 

#### Tez：
Tez 产生的主要原因是绕开 MapReduce 所施加的限制。Tez 项目的目标是支持高度定制化，这样它就能够满足各种用例的需要，让人们不必借助其他的外部方式就能完成自己的工作。<br>
参考资料：[spark与tez比较](http://www.zdingke.com/2016/12/05/spark%E4%B8%8Etez%E6%AF%94%E8%BE%83/?ysvulg=qgp7x1 "spark与tez比较"). 

#### Spark VS TeX
Spark更像是一个通用的计算引擎，提供内存计算，实时流处理，机器学习等多种计算方式，适合迭代计算
Tez作为一个框架工具，特定为hive和pig提供批量计算

#### Kylin
Kylin和Hive功能是类似的，提供Hadoop/Spark之上的SQL查询接口及多维分析（OLAP）能力以支持超大规模数据。<br>
通过构建一个数据立方体模型，来实现数据的快速查询和相应,理论上能获得比Hive更好的性能 <br>

### ETL
#### Sqoop
Sqoop是一个用来将Hadoop和关系型数据库中的数据相互转移的开源工具，<br>
可以将一个关系型数据库（例如 ： MySQL ,Oracle ,Postgres等）中的数据导进到Hadoop的HDFS中，也可以将HDFS的数据导进到关系型数据库中。<br>
参考资料：[使用Sqoop从MySQL导入数据到Hive和HBase 及近期感悟](https://www.zybuluo.com/aitanjupt/note/209968 "使用Sqoop从MySQL导入数据到Hive和HBase 及近期感悟"). 

#### Pig
是在MaoReduce之上的一层，把Java API 进行了封装，简化了MapReduce的开发，使得开发者能够通过简单的Pig-Latin语言就能操控集群上的数据。<br>
看起来好像和Hive有点像，但是实际上Pig 更像一种脚本工具，而Hive是数据仓库。<br>
参考资料：[Apache Pig入门1 –介绍/基本架构/与Hive对比](https://blog.csdn.net/joeyon1985/article/details/41805743 "Apache Pig入门1 –介绍/基本架构/与Hive对比"). 

Mahout：
ZooKeeper：
Avro：
Flume：
Pig：
Kafka：
Impala：



