import threading
import time

class Demo(threading.Thread):
    def __init__(self,val):
        # threading.Thread.__init__(self)
        super().__init__()
        self.val = val

    def run(self):
        print(f'子类执行了{self.val}')
        time.sleep(3)
        print(f'子类执行结束{self.val}')

d1 = Demo(1)
d2 = Demo(2)
d1.setDaemon(True)
d1.start()
d2.start()

d1.join()
print('结束')

