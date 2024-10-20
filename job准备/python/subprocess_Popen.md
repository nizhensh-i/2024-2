subprocess

**subprocess.Popen()**

1.args

​	1.1 字符串形式   会被当做是可执行文件的路径，这样就不能传入任何参数了。



​	1.2 列表形式       则第一项被视为命令，其余的都视为是给shell本身的参数。

   		`subprocess.Popen([``"/bin/sh"``, ``"-c"``, ``"cat test.txt"``])`

​		也就是说，等效于：

​		`subprocess.Popen([``'/bin/sh'``, ``'-c'``, args[``0``], args[``1``], ...])`

​	在windows下，`subprocess.Popen(``"cat test.txt"``)` 执行会失败的，因为如果是一个字符串的话，必须是程序的路径才可以



总结：建议用列表形式传参：

​		`subprocess.Popen(['/bin/sh', '-c', args[0], args[1], ...])`