



# 持久化数据

用卷

~~~
# 创建卷
docker volume create mysql_data

--mount type=volume,src=database_v,target=/etc/.. 
~~~



# 实时更新代码改变

1.用绑定安装 。这会将宿主机目录与容器某个目录进行共享，主机的改动会立即反映在容器的目录中，反之亦然。

~~~

--mount type=bind
~~~

2.但这并不能并不能反映代码层间的更改。如果需要看到代码的更改反映在页面上，需要开始nodemon监视文件系统的更改

~~~


~~~



# 网络，容器间通信。

把容器放到网络上有两种方式

- 启动容器时分配网络
- 将已运行的容器连接到网络

1.创建网络

~~~
docker network create database_n
~~~



2.启动MySql容器并分配网络

~~~
# 即使未执行创建卷的步骤，docker识别出想要创建命名卷mysql_data ，并自动创建一个
# --network-alias mysql 可以理解为该容器在网络上的别名为mysql，同网络下的其他容器使用该名字即可映射到此容器
docker run --name mysql -d --network database_n --network-alias mysql -v mysql_data:/var/lib/mysql -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=flasky -e MYSQL_USER=flasky -e MYSQL_PASSWORD=1234 mysql/mysql-server:latest
~~~




3.(可选)使用DNS工具--- dig命令

~~~
# 查找主机名为mysql的ip地址
dig mysql
~~~

4.当删除mysql镜像，重新运行一个镜像时，必须知道之前的卷才能才能读取之前的数据

~~~
docker run --name mysql -d --network database_n --network-alias mysql  -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=flasky -e MYSQL_USER=flasky -e MYSQL_PASSWORD=1234  mysql/mysql-server:latest
~~~

5.开始一个redis实例

~~~~
# 开始一个redis实例
docker run --name some-redis -d redis



# 使用自己的redis.conf
#第一个-v是把本机redis.conf映射到容器配置文件位置，第二个-v是创建一个名为redis_data的持久卷
docker run --network database_n --network-alias myredis -v E:\ruanjian\redis\redis.conf:/usr/local/etc/redis/redis.conf -v redis_data:/data --name my-redis -d redis redis-server /usr/local/etc/redis/redis.conf  --save 60 1 --loglevel warning


redis.conf
bind 0.0.0.0
~~~~



6.后端项目连接MySql,Redis

  记住:`每个容器都有自己的ip地址`

~~~

# 运行后端容器并连接MySQL
docker run --name backend -d -p 192.168.1.13:8081:5000 --network database_n  -e DATABASE_URL=mysql+pymysql://flasky:1234@mysql/flasky -e MAIL_USERNAME=zmc_li@foxmail.com -e MAIL_PASSWORD=jakkuvskichwbbaa -e REDIS_URL=redis://:1234@myredis:6379/0  flasky:latest
~~~





