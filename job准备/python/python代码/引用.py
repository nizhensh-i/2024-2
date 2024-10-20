class Test(object):
    def __init__(self):
        print(f'id是:{id(self)}')


    def __new__(cls,*args,**kwargs):
        print('__new__执行了')
        return super().__new__(cls)

# t1 = Test()
# t2 = Test()
# t3 = Test() * 10

# t1 = Test()
    

# a = 1
# print(id(1))
# print(id(a))
# a = 2
# print(id(a))

x = [1,2,3,[4,5,6]]
y = list(x)
print(y)
print(x == y)
print(y[-1] is x[-1])

l1 = [3,[66,44],(7,8,9),100]
l2 = [3,[55,44],(7,8,9)]


l1 = [3,[66,33,32,22],(7,8,9,10,11),100]
l2 = [3,[66,33,32,22],(7,8,9,10,11),100]


a = [10, 20]
b = [a, 30]
a.append(b)
# print(a)

from copy import deepcopy
c = deepcopy(a)
print(c)
