class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CycleLinkedList:
    # 循环单链表(带头结点)   判空条件:节点的next指向头结点
    def __init__(self, value=None):
        self.head = Node(value)
        self.head.next = self.head

    def head_add(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def tail_add(self, value):
        new_node = Node(value)
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

    def travel(self):
        result = []
        cur = self.head
        while cur.next != self.head:
            result.append(cur.next.value)
            cur = cur.next
        return result

    def is_empty(self):
        if self.head.next == self.head:
            return True
        return False

    def length(self):
        count = 0
        cur = self.head
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count
