class Deque:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return not len(self.data)

    def enqueue_front(self, value):
        self.data.insert(0, value)

    def enqueue_rear(self, value):
        self.data.append(value)

    def dequeue_front(self):
        if self.is_empty():
            return False
        return self.data.pop(0)

    def dequeue_rear(self):
        if self.is_empty():
            return False
        return self.data.pop()

    def size(self):
        return len(self.data)
