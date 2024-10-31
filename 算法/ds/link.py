class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    # 单链表(带头结点的)
    def __init__(self):
        self.head = Node()

    def head_add(self, value):
        # 头插法
        new_node = Node(value)

        new_node.next = self.head.next
        self.head.next = new_node

    def tail_add(self, value):
        # 尾插法
        new_node = Node(value)

        # 指向头结点
        cur = self.head

        # 使cur指向最后一个节点
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def search(self, value):
        # 在链表中查找值等于value,找到则返回True,否则False
        cur = self.head
        while cur.next:
            if cur.next.value == value:
                return True
            cur = cur.next
        return False

    def is_empty(self):
        # 空链表返回True，否则返回Flase
        if self.head.next:
            return False
        return True

    def length(self):
        count = 0
        cur = self.head
        while cur.next:
            count += 1
            cur = cur.next
        return count

    def insert(self, pos, value):
        # 在第pos个位置插入value值
        if pos < 1:
            self.head_add(value)
        elif pos > self.length():
            self.tail_add(value)
        else:
            p = self.get_node(pos - 1)
            new_node = Node(value)
            new_node.next = p.next
            p.next = new_node

    def travel(self):
        result = []
        cur = self.head
        while cur.next:
            result.append(cur.next.value)
            cur = cur.next
        return result

    def remove(self, value):
        cur = self.head
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next
                return True
            cur = cur.next
        return False

    def get_node(self, index):
        # 按序号查找节点值
        cur = self.head
        count = 0
        while cur.next:
            count += 1
            if count == index:
                return cur.next
            cur = cur.next
        return None


if __name__ == '__main__':
    link = LinkedList()
    link.tail_add(1)
    link.tail_add(10)
    link.tail_add(11)
    link.tail_add(6)
    link.insert(3, 7)
    link.insert(-5, 9)
    link.insert(19, 19)
    link.remove(9)

    # print(link.search(1))
    # print(link.is_empty())
    #
    #
    # print(link.length())

    cur = link.head
    link.travel()
    node = link.get_node(2)
