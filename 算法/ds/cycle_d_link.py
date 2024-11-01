class Node:
    def __init__(self, value=None):
        self.value = value
        self.pre = None
        self.next = None


class CycleDLink:
    # 循环双向链表(带头结点)
    def __init__(self, value=None):
        self.head = Node(value)
        self.head.pre = self.head
        self.head.next = self.head

    def head_add(self, value):
        new_node = Node(value)
        new_node.pre = self.head
        new_node.next = self.head.next
        self.head.next = new_node
        # 只会执行一次
        if self.head.pre == self.head:
            self.head.pre = new_node
    def tail_add(self, value):
        tail = self.head.pre
        new_node = Node(value)
        new_node.pre = tail
        new_node.next = tail.next
        tail.next = new_node
        self.head.pre = new_node

    def is_empty(self):
        # 空链表返回True，否则返回Flase
        return self.head.next == self.head and self.head.pre == self.head

    def length(self):
        count = 0
        cur = self.head
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        result = []
        cur = self.head
        while cur.next != self.head:
            result.append(cur.next.value)
            cur = cur.next
        return result

    def remove(self, value):
        cur = self.head
        while cur.next != self.head:
            if cur.next.value == value:
                # 删除中间节点
                if cur.next.next:
                    cur.next.next.pre = cur
                    cur.next = cur.next.next
                # 删除的是最后一个节点
                else:
                    cur.next = cur.next.next
                    self.head.pre = self.head
                return True
            cur = cur.next
        return False




