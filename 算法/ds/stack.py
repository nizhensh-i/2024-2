class Stack:
    """
    栈：先进后出
    使用list实现，其中list的append就是栈的push；list的pop就是栈的pop；list的[-1]就是栈的peek
    """
    MAX_SIZE = 7

    def __init__(self):
        self.data = []

    def push(self, value):
        if len(self.data) == Stack.MAX_SIZE:
            return False
        self.data.append(value)
        return True

    def pop(self):
        if not self.size():
            return False
        return self.data.pop()

    def get_top(self):
        if not self.size():
            return False
        return self.data[-1]

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.data)

