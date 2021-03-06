### 数据库 ###
所谓“数据库”系以一定方式储存在一起、能予多个用户共享、具有尽可能小的冗余度、与应用程序彼此独立的数据集合。

数据是指对客观事件进行记录并可以鉴别的符号，是对客观 事物的性质、状态以及相互关系等进行记载的物理符号或这些物 理符号的组合。它是可识别的、抽象的符号。

### 数据库分类 ###
最常见的数据库模型主要是两种，即关系型数据库和非关系型数据库。

当前在成熟应用且服务与各种系统的主力数据库还是关系型数据库。

- 关系型数据库
	- Oracle、SQL Server、MySQL
- 非关系型数据库
	- 键值（KV）存储：Memcached、Redis
	- 列存储（column-oriented）：HBASE(新浪，360)、Cassandra（200台服务器集群 ）
	- 文档数据库（document-oriented）：MongoDB（最接近关系型数据库的NoSQL）
	- 图形存储（Graph）：Neo4j

NoSQL数据库在存储速度与灵活性方面有优势，也常用于缓存。


### PostgreSQL ###
**免费开源的对象关系性数据库**

PostgreSQL是一个功能强大的开源对象关系数据库管理系统(ORDBMS)。 用于安全地存储数据，支持最佳做法，并允许在处理请求时检索它们。

PostgreSQL(也称为Post-gress-Q-L)由PostgreSQL全球开发集团(全球志愿者团队)开发。 它不受任何公司或其他私人实体控制。它是开源的，其源代码是免费提供的。

PostgreSQL是跨平台的，可以在许多操作系统上运行，如Linux，FreeBSD，OS X，Solaris和Microsoft Windows等。

### MySQL ###
**Oracle收购前免费开源，Oracle收购后，社区版免费开源，商业版收费的关系型数据库**

MySQL是一个关系型数据库管理系统，由瑞典MySQL AB 公司开发，目前属于 Oracle 旗下产品。MySQL 是最流行的关系型数据库管理系统之一，在 WEB 应用方面，MySQL是最好的 RDBMS (Relational Database Management System，关系数据库管理系统) 应用软件之一。

MySQL所使用的 SQL 语言是用于访问数据库的最常用标准化语言。MySQL 软件采用了双授权政策，分为社区版和商业版，由于其体积小、速度快、总体拥有成本低，尤其是开放源码这一特点，一般中小型网站的开发都选择 MySQL 作为网站数据库。

MySQL以前一直是开源免费的，被Oracle收购后有些变化：以前的版本都是免费的，社区版按GPL协议开源免费，商业版提供更加丰富的功能，但收费。


范式可以指导我们更好地设计数据库的表结构，减少冗余的数据，借此可以提高数据库的存储效率，数据完整性和可扩展性。


Mysql数据库，可以通过配置，实现远程登录，但root帐户是无法远程登陆的，只可以本地登陆

- mysql是一个典型的c/s模式，服务端与客户端两部分组成
	- 服务端程序 mysqld
	- 客户端程序 mysql自带客户端（mysql、mysqladmin、mysqldump等） 第三方客户端  API接口（php-mysql）

- mysql连接方式
	- TCP/IP 连接   网络连接串(通过用户名 密码 IP 端口进行连接)
		- mysql -uroot -p123 -h 127.0.0.1 -P 3306
	- socket 连接   网络套接字(用户名 密码  socket文件)
		- mysql -uroot -p123 -S /application/mysql/tmp/mysql.sock 

-  MySQL在启动过程
	-  启动后台守护进程，并生成工作线程
	-  预分配内存结构供MySQL处理数据使用
	-  实例就是MySQL的后台进程+线程+预分配的内存结构

- mysqld服务架构
	1. 连接层
		1. 通信协议
			1. TCP/IP
			2. socket
		2. 线程
		3. 验证
	2. SQL层
		1. 解析器
		2. 优化器
		3. 授权
		4. 查询执行
		5. 查询高速缓存
		6. 查询日志记录
	3. 存储引擎层
		1. 磁盘
			1. InnoDB
			2. MyISAM
		2. 内存
			1. MEMORY
		3. 网络
			1. NDB

[参阅](https://www.cnblogs.com/clsn/p/8038964.html#auto_id_0)

### Redis ###
**免费开源的键值存储的非关系型数据库**

Redis 是完全开源免费的，遵守BSD协议，是一个高性能的key-value数据库。

- Redis 与其他 key-value 缓存产品有以下三个特点：
	- Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
	- Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
	- Redis支持数据的备份，即master-slave模式的数据备份

- 优势
	- 性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
	- 丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
	- 原子 – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。多个操作也支持事务，即原子性，通过MULTI和EXEC指令包起来。
		- 如果把一个事务可看作是一个程序,它要么完整的被执行,要么完全不执行。这种特性就叫原子性。
		- 要么一起成功，要么一起失败的操作叫原子性操作
	- 丰富的特性 – Redis还支持 publish/subscribe, 通知, key 过期等等特性。

- Redis与其他key-value存储有什么不同？
	- Redis有着更为复杂的数据结构并且提供对他们的原子性操作，这是一个不同于其他数据库的进化路径。Redis的数据类型都是基于基本数据结构的同时对程序员透明，无需进行额外的抽象。
	- Redis运行在内存中但是可以持久化到磁盘，所以在对不同数据集进行高速读写时需要权衡内存，因为数据量不能大于硬件内存。在内存数据库方面的另一个优点是，相比在磁盘上相同的复杂的数据结构，在内存中操作起来非常简单，这样Redis可以做很多内部复杂性很强的事情。同时，在磁盘格式方面他们是紧凑的以追加的方式产生的，因为他们并不需要进行随机访问

[参阅](http://www.runoob.com/redis/redis-intro.html)


### MongoDB ###
**免费开源的分布式文件存储的非关系型数据库**


MongoDB 是一个基于分布式文件存储的数据库。由 C++ 语言编写。旨在为 WEB 应用提供可扩展的高性能数据存储解决方案。

MongoDB是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库当中功能最丰富，最像关系数据库的。他支持的数据结构非常松散，是类似json的bjson格式，因此可以存储比较复杂的数据类型。Mongo最大的特点是他支持的查询语言非常强大，其语法有点类似于面向对象的查询语言，几乎可以实现类似关系数据库单表查询的绝大部分功能，而且还支持对数据建立索引。

- 层次结构
	1. 文档
	2. 集合
	3. 数据库

MongoDB服务端可运行在Linux、Windows或OS X平台，支持32位和64位应用，默认端口为27017。

网上很多人不建议

### 优化 ###
**优化数据库（清理用户及无用数据库）**

### 数据处理调优 ###
**避免全表扫描、精确更新、使用耗内存少的数据类型**

1. 对查询进行优化，要尽量避免全表扫描，首先应考虑在 where 及 order by 涉及的列上建立索引。
2. 应尽量避免在 where 子句中对字段进行 null 值判断，否则将导致引擎放弃使用索引而进行全表扫描
3. 应尽量避免在 where 子句中使用 != 或 <> 操作符，否则将引擎放弃使用索引而进行全表扫描。
4. 应尽量避免在 where 子句中使用 or 来连接条件，如果一个字段有索引，一个字段没有索引，将导致引擎放弃使用索引而进行全表扫描
5. in 和 not in 也要慎用，否则会导致全表扫描
6. 应尽量避免在where子句中对字段进行函数操作，这将导致引擎放弃使用索引而进行全表扫描
7. 尽量避免大事务操作，提高系统并发能力。
8. 尽量避免向客户端返回大数据量，若数据量过大，应该考虑相应需求是否合理。
9. 避免频繁创建和删除临时表，以减少系统表资源的消耗
10. 任何地方都不要使用 select * from t ，用具体的字段列表代替“*”，不要返回用不到的任何字段。
11. 尽量使用表变量来代替临时表。如果表变量包含大量数据，请注意索引非常有限（只有主键索引）。
12. 尽可能的使用 varchar/nvarchar 代替 char/nchar
13. 尽量使用数字型字段
14. Update 语句，如果只更改1、2个字段，不要Update全部字段，否则频繁调用会引起明显的性能消耗，同时带来大量日志。
15. 对于多张大数据量（这里几百条就算大了）的表JOIN，要先分页再JOIN，否则逻辑读会很高，性能很差。 
16. 应尽可能的避免更新 clustered 索引数据列

[参阅](https://blog.csdn.net/zhushuai1221/article/details/51740846)