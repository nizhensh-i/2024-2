class Singleton:
    _instance = None

    def __new__(cls,*args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls,*args,**kwargs)
        return cls._instance

class TestA(Singleton):
    c = 1

a = TestA()
b = TestA()

print(a is b)
print(a)
print(b)