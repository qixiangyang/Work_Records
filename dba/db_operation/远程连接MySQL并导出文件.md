
### 任务背景

   需要导出正式服务器上的一些数据，尝试使用普通用户使用远程登陆的方式导出数据，但是提示权限不足：
   ~~~
   ERROR 1045 (28000): Access denied for user 'quantuser'@'%' (using password: YES)
   ~~~
   所以考虑直接登陆到正式服务器上导出数据，由于正式数据库无法直联，通过跳板机的方式登陆，之前没有
   遇到过，这次将过程记录下来。

1. 通过跳板机登陆正式服务器
   ~~~
   命令： ssh root@10.1.1.7
   ~~~
 
2. 登陆MySQL
   命令 mysql -uroot -p
   
3. 执行sql语句
    ~~~
     select * from k_line_day where symbol in 
    (SELECT symbol FROM company_industry WHERE industry_name = '建筑装饰') 
    into outfile "/data/mysql/total_volume_0909.csv" fields terminated by ',' 
    optionally enclosed by '"' escaped by '"' lines terminated by "\r\n";
    ~~~

4. 将导出文件从正式服务器导出到测试服务器root目录下
   ~~~
   scp root@10.1.1.7:/data/mysql/total_volume_0909.csv ./
   ~~~
