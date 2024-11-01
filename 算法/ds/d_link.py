class Node:
    def __init__(self, value=None):
        self.value = value
        self.pre = None
        self.next = None


class DLinkedList:
    def __init__(self, value=None):
        self.head = Node(value)

    def head_add(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        new_node.pre = self.head
        self.head.next = new_node

    def tail_add(self, value):
        cur = self.head
        while cur.next:
            cur = cur.next
        new_node = Node(value)
        new_node.pre = cur
        cur.next = new_node

    def is_empty(self):
        # 空链表返回True，否则返回Flase
        return not self.head.next

    def length(self):
        count = 0
        cur = self.head
        while cur.next:
            count += 1
            cur = cur.next
        return count

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
                # 删除中间节点
                if cur.next.next:
                    cur.next.next.pre = cur
                    cur.next = cur.next.next
                # 删除的是最后一个节点
                else:
                    cur.next = cur.next.next
                return True
            cur = cur.next
        return False
