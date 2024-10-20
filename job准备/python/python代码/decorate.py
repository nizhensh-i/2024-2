import time
# 函数重复执行多少次？
def more(nums = 5):
    def decorate(func):
        def address():
            for i in range(nums):
                func()
            print(f'执行了{nums}次')
        return address
    return decorate

@more()
def func():
    print('普通函数执行了')



class Clock:
    
    def __init__(self,func):
        self.func = func

    def __call__(self,*args,**kwargs):
        print('实例对象执行了')
        time.sleep(1)
        print('实例方法将退出...')
        
        return self.func(*args,**kwargs)



@Clock
def sleep():
    print('原函数执行了')

if __name__ == '__main__':
    # func()
    sleep()

