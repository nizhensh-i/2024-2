class Queue:
    # 顺序队列。  Python列表作为队列定义，不会存在"假溢出"的情况，所以免去在Python中实现循环队列的定义
    def __init__(self, capacity=7):
        self.data = []
        self.capacity = capacity

    def is_empty(self):
        return not len(self.data)

    def is_full(self):
        return len(self.data) == self.capacity

    def enqueue(self, value):
        if self.is_full():
            return False
        self.data.append(value)
        return True

    def dequeue(self):
        if self.is_empty():
            return False
        return self.data.pop(0)

    def size(self):
        return len(self.data)
