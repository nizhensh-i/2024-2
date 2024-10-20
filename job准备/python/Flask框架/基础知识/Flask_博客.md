2024年6月10日23:05:40 **端午3天假**

1. Flask 应用打包成wheel文件(.whl)
   .whl可以直接在在别的机器上安装该应用和所依赖的包。在docker容器中也可以直接安装这个应用。相当于Vue应用的dist下的文件。  
    ~~~
   # 执行
   python setup.py bdist_wheel
~~
2. pytest
    测试所有可能的情况
    统计覆盖率。文件夹和函数都以test开头。
3. 蓝图
    是一种组织视图和其他代码的一种方式。比如所有的视图函数都放在一起同一个模块下(.py)。
    先将相关视图在蓝图中注册，最后将试图注册在工厂函数中
4. 视图
    处理请求的函数。典型的是url映射到的处理函数。视图名字默认就是视图函数的名字。
5. 端点
     就是视图的名字，比如hello()函数，那么端点就是hello,一般在url_for()函数中使用，是将端点转为url。在蓝图中，端点的格式为:蓝图名字.视图
6. 工厂函数
     在对象中创建对象实例，并返回。
7. jinja2
     {% 条件表达式 %}
     html模版可以继承
8. sqllite3数据库
     连接数据库
     执行sql: db.exescrits()
9.  在powershell中设置环境变量
~~~
# 设置
$env:FLASK_APP="flaskr"

#打印
echo $env:FLASK_APP
~~~
10.  在cmd命令函中设置环境变量
~~~
# 设置
set FLASK_APP=flaskr

# 打印
echo %FLASK_APP%
~~~