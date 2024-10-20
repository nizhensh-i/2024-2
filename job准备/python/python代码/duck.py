class Duck:
    a = 1
    def __init__(self):
        pass

class D_son(Duck):
    def __init__(self):
        pass
    pass


print(isinstance(D_son(),Duck))
print(D_son.mro())