class ShareStack:
    # 利用一维链表空间，实现共享栈
    def __init__(self, max_size=10):
        self.data = [None] * max_size
        # 栈的最大容量
        self.max_size = max_size
        self.top1 = -1
        self.top2 = max_size

    def push1(self, value):
        if self.top1 == self.top2 - 1:
            return False
        self.top1 += 1
        self.data[self.top1] = value
        return True

    def push2(self, value):
        if self.top1 == self.top2 - 1:
            return False
        self.top2 -= 1
        self.data[self.top2] = value
        return True

    def pop1(self):
        if self.top1 == -1:
            return False
        res = self.data[self.top1]
        self.data[self.top1] == None
        self.top1 -= 1
        return res

    def pop2(self):
        if self.top2 == self.max_size:
            return False
        res = self.data[self.top2]
        self.data[self.top2] == None
        self.top2 += 1
        return res

    def is_empty1(self):
        return self.top1 == -1

    def is_empty2(self):
        return self.top2 == self.max_size

    def size(self):
        return self.max_size - self.top2 + 1 + self.top1
