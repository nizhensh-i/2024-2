class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self,value=None):
        self.root = Node(value)


def mid(root):
    if root.value:
        mid(root.left)
        print(root.value)
        mid(root.right)





#在b中查找a, 找到返回首位置，否则返回-1



# def find(a,b):
#     if not a:
#         return
#     i, j = 0, 0
#     len_a = len(a)
#     while j < len(b):
#         if i == len_a:
#             return j - len_a
#         if b[j] == a[i]:
#             j += 1
#             i += 1
#         else:
#             j += 1
#             i = 0
#     return -1

a = '  '
b = 'abcdef'

def index(text, sub_str):
    if not sub_str or not isinstance(sub_str,str):
        return -1
    len_a = len(text)
    len_b = len(sub_str)
    i, j = 0, 0
    while i < len_a and j < len_b:
        if text[i] == sub_str[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    if j >= len_b:
        return i - len_b
    return -1

print(index(b, a))