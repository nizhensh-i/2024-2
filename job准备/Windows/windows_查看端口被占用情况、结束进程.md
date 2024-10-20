# windows_查看端口被占用情况、结束进程

查看指定端口占用情况

~~~
netstat -aon | findstr 8081
netstat -aon | findstr 6379
~~~

根据PID查看相应的进程或程序

~~~
tasklist | findstr 21836
~~~

命令结束

```
 taskkill /f /t /im 进程名(PID)
 或者
 taskkill /f /t /im svchost.exe(要结束的程序)
```


# 电脑开机后，只有qq能登陆，浏览器网页打不开

解决：关闭 使用代理服务器

![72705666013](C:\Users\19125\Desktop\2024-2月面试\job准备\Windows\windows_查看端口被占用情况、结束进程.assets\1727056660133.png)



# redis 安装

1.安装包在自己百度云盘   normal_tools/redis 

- 解压安装包
- 安装可视化软件

2.去安装目录 ，修改`redis.conf`文件

-  创建 日志目录   ，`只需要`创建redis_log文件夹， `不需要`创建redis_log.log 文件
  - logfile ../redis_log/redis_log.log 
- 创建rdb文件存放目录
  - dir ../redis_data/    
-  设置连接密码。连接时需要输入密码     ` redis-cli.exe -a 1234`
  - requirepass  1234      
-  (可选)为了更好管理和调式Redis服务器。我们希望将Redistribution服务器的ip修改为本机的ip地址
   -  将bind参数改为本机ip地址

![72732250757](C:\Users\19125\Desktop\2024-2月面试\job准备\Windows\windows_查看端口被占用情况、结束进程.assets\1727322507574.png)

3.登录可视化软件

![72732271470](C:\Users\19125\Desktop\2024-2月面试\job准备\Windows\windows_查看端口被占用情况、结束进程.assets\1727322714707.png)



启动redis:

~~~
# 在安装目录运行此命令
redis-server.exe redis.conf
~~~





