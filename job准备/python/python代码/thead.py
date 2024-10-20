import threading
import time

def test1():
    print('1执行了')
    time.sleep(3)
    print('1结束了')

def test2():
    print('2执行了')
    time.sleep(3)
    print('2结束了')


# t1 = threading.Thread(target=test1)
# t2 = threading.Thread(target=test2)

# t1.start()
# t2.start()

# print('结束')

class B:
    def __enter__(self):
        print('进入')
    
    def __exit__(self,exc_type,exc_value,traceback):
        print('退出了')

# class A:
#     def __init__(self):
#         pass
# a = A()
# b= B()

# a + b
    
with B() as b:
    # raise
    print('进入代码块了')


# l = [0,2,13,24,45]
# l.insert(2,10)
# print(l)
# print(l.index(10))
# l.insert(3,12)
# print(l.index(24))

""" import json

json_str = '{"name":"jack","age":"12"}'

# 将json字符串变成字典
j = json.loads(json_str)
print(j)

# 12
print(j['age'])

# 将python结构转换成JSON字符串
j_str = json.dumps(j)
print(j_str)

# <class 'str'>
print(type(j_str))   """




d = {'age':12,'sex':1,'school':'123'}
f = d.get('sex')
print(f)
print(d)
