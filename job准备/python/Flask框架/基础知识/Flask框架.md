#                             Flask框架

1. 状态码

   重定向：302

   成功：200

   无效：400

   错误码：404

2. SQLALchemy。

   使用url来指定数据库

3. 视图和蓝图

   1. 视图是应用对请求响应的函数。
   2. 把一个应用分解为一套蓝图。这是针对大型应用的理想方案：一个项目可以实例化 一个应用，初始化多个扩展，并注册许多蓝图。
   3. 蓝图：是一种组织一组相关视图及其他代码的方式。与把视图及其他 代码直接注册到应用的方式不同，蓝图方式是把它们注册到蓝图，然后在工厂函数中 把蓝图注册到应用。

4. 环境变量的读取

   账号密码不便于明文写在程序里时，将账号密码保存在环境变量中。

   环境变量是程序与操作系统的通信方式。

   ~~~
   import os

   name = os.environ.get('USERNAME')
   print(name)
   ~~~


   #get当此键值为None时，会采用第二个参数
   name = os.environ.get('SQLNAME_1','123')
   print(name)
   ~~~

   **千万不要把密码或其他机密信息写在纳入版本控制的配置文件中**




4.  **python单脚本应用VS. 大型应用的结构**

5. os.path 库

   1. `os.path.split(path)`

      将路径 *path* 拆分为一对，即 `(head, tail)`，其中，*tail* 是路径的最后一部分，而 *head* 里是除最后部分外的所有内容。*tail* 部分不会包含斜杠，如果 *path* 以斜杠结尾，则 *tail* 将为空。

   ~~~
   >>print(os.path.split(__file__))
   >> >>('c:\\Users\\19125\\Desktop\\job准备\\python\\Flask框架\\代码\\app','email.py')  
   >> ~~~
   >>
   >> ~~~

   2. `os.path.dirname(path)`

       返回路径 *path* 的目录名称。这是将 *path* 传入函数 [`split()`](https://docs.python.org/zh-cn/3.9/library/os.path.html#os.path.split) 之后，返回的一对值中的第一个元素。

      ~~~
      #__file__:  c:\Users\19125\Desktop\job准备\python\Flask框架\代码\app\email.py
      #返回当前文件目录的路径  
      >>print(os.path.dirname(__file__))
      >>c:\Users\19125\Desktop\job准备\python\Flask框架\代码\app
      ~~~

   3. `os.path.join(path,*path)`

      智能地拼接一个或多个路径部分。

      ~~~
      >>print(os.path.join(os.path.dirname(__file__),'abc','ad'))
      >>c:\Users\19125\Desktop\job准备\python\Flask框架\代码\app\abc\ad
      ~~~

   4. `os.path.abspath(path)`

      返回路径 *path* 的绝对路径（标准化的）

      ~~~

      ~~~

      d 

6. 分页显示？

   比如当页面表格显示全部的数据行时，页面的加载速度会变慢。在Web浏览器中，内容多的网页需要花费更多的时间生成，下载和渲染，因此网页内容变多会让用户体验变差。

   解决办法：分页显示数据

7. 项目值得做测试吗？

   不管你喜不喜欢，应用肯定是要做测试的。如果你自己不做测试，用户就要充当不情愿的测试员，用户发现问题后，你就要顶着压力修改。

   测试绝对值得。重要的是我们要设计一个**高效的测试策略**，还要**编写能合理利用这一策略的代码**。

8. 性能

   没有人喜欢运行缓慢的应用。页面加载时间太长会让用户失去兴趣，应该尽早发现并修正性能问题。

   1. 数据库查询变慢了。


   2. 分析源码。可能是高CPU消耗，又执行大量运算的函数导致。

   3. 部署

   1. 云部署：把应用部署到一台或多台虚拟服务器上。虚拟服务器操作起来的感受与物理设备很想，但却是由云服务公司管理的虚拟设备。
   2. 更高级的部署方式是基于容器。一个容器把应用隔离在一个映像中，里面包含应用及其全部依赖。你可以安装容器平台，比如Docker。
      6. 另外一种部署方式，Paas(平台及服务)。服务商完全接管了运行应用的平台。应用开发者只需把应用代码上传到服务器提供商维护的服务器中，整个过程往往只需要几秒钟。





1.消息闪现

​	有且只在下一个请求中访问上一个请求结束是记录的消息。

​	注意：当消息比会话cookie大时，那么会导致消息闪现静默失败

​	疑问：消息闪现在前后端分离的模式下还有用吗？前端完全可以保存将上一个请求的结果，同时热更新页面

2.信号

​	当一个事件发生时，发射信号，信号调用所有的订阅者。

​	优势：可以被临时订阅，并且不能直接影响应用程序。

​	应用场景：测试，度量，审计



# 通过 dotenv 设置环境变量

1.在应用文件的同级目录创建`.env`文件，该文件格式如下：

~~~
FLASK_APP=flasky.py
FLASK_DEBUG=1
FLASK_RUN_PORT=8765
~~~

 也支持变量，变量必须用`{}`括起来，类似的bash的语法：

~~~
DOMAIN=example.org
ADMIN_EMAIL=admin@${DOMAIN}
~~~

2.应用文件中引入该文件

~~~
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)  

# 验证环境变量
print(os.getenv("FLASK_RUN_PORT"))
~~~



