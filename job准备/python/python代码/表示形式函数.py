
class Vector:
    
    code = 1
    _private = 2
    __privite =3
    def __init__(self):
        self.instance = 2
        pass

    def __repr__(self):
        print('repr执行了')
        return '2'

    def __str__(self):
        print('str执行了')
        return '1'

v = Vector()

# print(v)
# print(repr(v))
# print(str(v))
# print(v.__dict__)


class A:
    __slot__ = ('_x','_y')

    def __init__(self,val1,val2):
        self._X = val1
        self._y = val2
        self._z = val1

a = A(1,2)



def func(a):
    return lambda x:x + a
f = func(1)
# print(f(5))


def delayed_start(*,func=None,  duration=1):

    print(func)
    print(duration)

delayed_start(func=1,duration = 2)
delayed_start()

print(callable(Vector))
print(callable(v))