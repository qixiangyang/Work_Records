# Hadoop生态学习记录

## Hadoop应用背景

数据的量随着技术的发展急剧增长，原来的单机尺度的数据分析时不能满足要求。<br>

Hadoop就是为了处理这种超过单机尺度的数据<br>

Hadoop及其生态已经事实上成为大数据体系的标准 <br>

![1](static/Hadoop.png)

## Hadoop的基本构成

### HDFS
HDFS是一种分布式文件系统，是数据存储的物理载体，在它的上层有Hbase、Hive等应用。<br>

### MapReduce
MapReduce，以下简称MR。负责计算数据，但是MR本身计算效率较低。在此基础上发展出了Tez和Spark，是第二代计算引擎。<br>

### YARN
Hadoop的资源监控与调度系统，替代原有的JobTracker。是Hadoop2.0新增的任务管理框架

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

### 计算引擎&操作MapReduce
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

#### Pig
是在MaoReduce之上的一层，把Java API 进行了封装，简化了MapReduce的开发，使得开发者能够通过简单的Pig-Latin语言就能操控集群上的数据。<br>
看起来好像和Hive有点像，但是实际上Pig 更像一种脚本工具，而Hive是数据仓库。<br>
参考资料：[Apache Pig入门1 –介绍/基本架构/与Hive对比](https://blog.csdn.net/joeyon1985/article/details/41805743 "Apache Pig入门1 –介绍/基本架构/与Hive对比"). 

#### Oozie
在 Hadoop 中执行的任务有时候需要把多个 Map/Reduce 作业连接到一起，这样才能够达到目的<br>
Oozie可以把多个 Map/Reduce 作业组合到一个逻辑工作单元中，从而完成更大型的任务。<br>
实际上就是一个工作流控制软件，工作流是放置在控制依赖 DAG（有向无环图 Direct Acyclic Graph）中的一组动作 （听起来和airflow有点像）<br>

### 任务调度&资源管理
#### ZooKeeper
ZooKeeper 是一个典型的分布式数据一致性解决方案，<br>
分布式应用程序可以基于 ZooKeeper 实现诸如数据发布/订阅、负载均衡、命名服务、分布式协调/通知、集群管理、Master 选举、分布式锁和分布式队列等功能。<br>
Zookeeper 一个最常用的使用场景就是用于担任服务生产者和服务消费者的注册中心。<br>
参考资料：[如果有人问你ZooKeeper是什么，就把这篇文章发给他。](https://juejin.im/post/5baf7db75188255c3d11622e "如果有人问你ZooKeeper是什么，就把这篇文章发给他。"). 

#### ZooKeeper VS YARN
分布式系统有很多问题 其中有两个
1. Coordination
2. Resource Management
Zookeeper偏重解决的是前者
Yarn偏重解决的是后者
参考资料：[Yarn和 Zookeeper之间是什么关系，都是管理节点，那他们的应用场景有何区别？](https://www.zhihu.com/question/41254423 "Yarn和 Zookeeper之间是什么关系，都是管理节点，那他们的应用场景有何区别？"). 

### 数据分析&建模

#### Impala
Impala是基于Hive的大数据实时分析查询引擎，直接使用Hive的元数据库Metadata,意味着impala元数据都存储在Hive的metastore中。 <br>
并且impala兼容Hive的sql解析，实现了Hive的SQL语义的子集，功能还在不断的完善中。 <br>
能够查询存储在Hadoop的HDFS和Hbase中的PB级大数据。查询速度快是其最大的卖点 <br>
参考资料：[impala的原理架构介绍及应用场景](https://blog.csdn.net/javajxz008/article/details/50523332 "impala的原理架构介绍及应用场景"). 
参考资料：[Impala - Impala和Hive的关系](https://www.jianshu.com/p/5fa3fa2dbd9a "Impala - Impala和Hive的关系"). 

#### Kylin
Kylin和Hive功能是类似的，提供Hadoop/Spark之上的SQL查询接口及多维分析（OLAP）能力以支持超大规模数据。<br>
通过构建一个数据立方体模型，来实现数据的快速查询和相应,理论上能获得比Hive更好的性能 <br>

#### Mahout
提供一些可扩展的机器学习领域经典算法的实现，旨在帮助开发人员更加方便快捷地创建智能应用程序。<br>
Mahout包含许多实现，包括聚类、分类、推荐过滤、频繁子项挖掘。此外，通过使用Apache Hadoop库。<br>
Mahout可以有效地扩展到云中。<br>

### ETL
#### Sqoop
Sqoop是一个用来将Hadoop和关系型数据库中的数据相互转移的开源工具，<br>
可以将一个关系型数据库（例如 ： MySQL ,Oracle ,Postgres等）中的数据导进到Hadoop的HDFS中，也可以将HDFS的数据导进到关系型数据库中。<br>
参考资料：[使用Sqoop从MySQL导入数据到Hive和HBase 及近期感悟](https://www.zybuluo.com/aitanjupt/note/209968 "使用Sqoop从MySQL导入数据到Hive和HBase 及近期感悟"). 



### 日志采集&消息队列

#### Flume：
Flume是开源日志系统。是一个分布式、可靠性和高可用的海量日志聚合系统，支持在系统中定制各类数据发送方，用于收集数据；同时，FLume提供对数据进行简单处理，并写到各种数据接收方（可定制）的能力。<br>
参考资料：[Flume技术原理](https://cshihong.github.io/2018/06/02/Flume%E6%8A%80%E6%9C%AF%E5%8E%9F%E7%90%86/ "Flume技术原理"). 


#### Kafka
Kafka主要用途是数据集成，或者说是流数据集成，以Pub/Sub形式的消息总线形式提供。<br>
但是，Kafka不仅仅是一套传统的消息总线，本质上Kafka是分布式的流数据平台，因为以下特性而著名：<br>
提供Pub/Sub方式的海量消息处理。<br>
以高容错的方式存储海量数据流。<br>
保证数据流的顺序。<br>
参考资料：[kafka解决了什么问题?](https://www.zhihu.com/question/53331259 "kafka解决了什么问题?"). 

#### Flume VS Kafka
业界比较典型的一中用法是：
线上数据 -> flume -> kafka -> hdfs -> MR离线计算 <br>
线上数据 -> flume -> kafka -> storm <br>
参考资料：[日志采集系统flume和kafka有什么区别及联系，它们分别在什么时候使用，什么时候又可以结合？](https://www.zhihu.com/question/36688175 "日志采集系统flume和kafka有什么区别及联系，它们分别在什么时候使用，什么时候又可以结合？"). 

### Hadoop集群管理&交互
#### Ambari

Ambari 是 Hortonworks 贡献给 Apache 开源社区的顶级项目，属于 Hadoop 生态中的重要组成部分，Hortonworks 本身也提供一些基于 Apache Hadoop 开发良好的商业应用组件，例如 HDP 数据平台。<br>
Ambari 不仅整合了常用的运维管理工具，更重要的本身专注于 Hadoop 集群管理方案，所以它的优势就在于 Hadoop 集群的供应、管理和监控等，最能解决我们的需求痛点。<br>
Ambari 基于 web 的特点能够直现给使用者直观用户界面，能够极大提升管理效率和降低本身开发成本。<br>

#### Ambari VS HUE VS Cloudera Manager(CM)

#### Ambari
Ambari 专注于Hadoop生态内各个组件的集成管理和部署，能够可视化的管理集群中各个节点的状态。和cloudera manager功能比较类似。<br>

#### Cloudera Manager
Cloudera Manager(简称CM)是Cloudera公司开发的一款大数据集群安装部署利器，这款利器具有集群自动化安装、中心化管理、集群监控、报警等功能<br>
使得安装集群从几天的时间缩短在几小时以内，运维人员从数十人降低到几人以内，极大的提高集群管理的效率。<br>

#### HUE 
一句话总结，HUE是用来操作Hadoop生态内各个组件的一个统一的可视化平台。
hue是hadoop生态系统的统一webUI。你可以通过hue的界面，链接hive，发出hive语句。<br>
我们可以在浏览器端的Web控制台上与Hadoop集群进行交互来分析处理数据，例如操作HDFS上的数据，运行MapReduce Job等等。<br>

简单来说Ambari 和 CM 是有直接的竞争关系。主要用于集群的搭建和监控，而HUE是用来和集群进行交互的，比如查询数据，配置MapReduce任务等。<br>

参考资料：[Cloudera Manager(简称CM)+CDH构建大数据平台](https://www.jianshu.com/p/1ed522c1ad1e "Cloudera Manager(简称CM)+CDH构建大数据平台"). <br>
参考资料：[hadoop web管理Hue,Ambari 和CM 的区别是什么?](https://www.zhihu.com/question/26794071 "hadoop web管理Hue,Ambari 和CM 的区别是什么?"). 

### 计算系统
#### Storm
Storm是一个分布式、可靠的实时计算系统。与Hadoop不同的是，它采用流式的消息处理方法，<br>
对于每条消息输入到系统中后就能被立即处理。适用于一些对实时性要求高的场景，比如广告点击在线统计、交易额实时统计等。 <br>
参考资料：[Hadoop、Storm和Spark 三者的区别、比较](https://blog.csdn.net/Coder__CS/article/details/78868346 "Hadoop、Storm和Spark 三者的区别、比较"). 

### 其他组件 (其实是不知道这个东西怎么用 逃)
#### Avro
Avro是一种远程过程调用和数据序列化框架，是在Apache的Hadoop项目之内开发的。它使用JSON来定义数据类型和通讯协议，使用压缩二进制格式来序列化数据。
它主要用于Hadoop，它可以为持久化数据提供一种序列化格式，并为Hadoop节点间及从客户端程序到Hadoop服务的通讯提供一种电报格式。

### 搜索引擎[不是Hadoop生态中的内容，只是为了厘清概念]

#### Solr
Solr（读作“solar”）是Apache Lucene项目的开源企业搜索平台。其主要功能包括全文检索、命中标示、分面搜索、动态聚类、数据库集成，以及富文本（如Word、PDF）的处理。<br>
Solr是高度可扩展的，并提供了分布式搜索和索引复制。Solr是最流行的企业级搜索引擎，Solr4 还增加了NoSQL支持。<br>

#### Elasticsearch(ES)：

Elasticsearch是一个实时的分布式搜索和分析引擎。它可以帮助你用前所未有的速度去处理大规模数据。 <br>
它可以用于全文搜索，结构化搜索以及分析，当然你也可以将这三者进行组合。<br>

#### Elasticsearch VS Solr
二者安装都很简单； <br>
Solr 利用 Zookeeper 进行分布式管理，而 Elasticsearch 自身带有分布式协调管理功能; <br>
Solr 支持更多格式的数据，而 Elasticsearch 仅支持json文件格式； <br>
Solr 官方提供的功能更多，而 Elasticsearch 本身更注重于核心功能，高级功能多有第三方插件提供； <br>
Solr 在传统的搜索应用中表现好于 Elasticsearch，但在处理实时搜索应用时效率明显低于 Elasticsearch。 <br>

参考资料：[搜索引擎选择： Elasticsearch与Solr](http://i.zhcy.tk/blog/elasticsearchyu-solr/ "搜索引擎选择： Elasticsearch与Solr"). 


