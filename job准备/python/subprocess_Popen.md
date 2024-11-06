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







~~~
import tempfile
import subprocess


def execute_command(command, no_exception=False, max_retry_count=1, name="funcName", timeout=1200, **kwargs):
    print(f"[{name}]:Execute command:{command}")
    log, status = "", None
    for i in range(max_retry_count):
        fileno = tempfile.NamedTemporaryFile(mode='wt+', delete=True)
        print("create temporary file")
        try:
            p = subprocess.Popen(args=[r"D:\rujian\Git\bin\bash.exe", "-c", command], shell=True, stdout=fileno,
                                 stderr=fileno, **kwargs)
            p.communicate(timeout=timeout)
            print("communicate subprocess finish")
            fileno.seek(0)
            log = fileno.read()
            status = p.returncode
            print(f"status:{status}, log:{log}")
            if status == 0:
                print(f"[{name}]:Execute command success! Command: {command}")
                break
            if not no_exception:
                raise Exception("命令执行失败")
            else:
                print(f"[{name}]:Execute command failed! Command fail!command:{command}")
                if (i + 1) == max_retry_count:
                    break
        except Exception as е:
            print('异常')
        finally:
            fileno.close()
    return status, log


if __name__ == '__main__':
    status, log = execute_command("cat a.txt", True)

~~~

