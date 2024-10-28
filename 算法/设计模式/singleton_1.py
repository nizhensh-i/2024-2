
def singleton(cls):
    instance = {}
    def decorate(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return decorate

@singleton
class TestC:
    x = 1


c = TestC()
d = TestC()

print(c is d)
print(c)
print(d)