class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkNode:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head

    def add_node(self,value):
        new = Node(value)
        self.tail.next = new
        self.tail = new


if __name__ == '__main__':
    link = LinkNode()
    link.add_node(2)
    link.add_node(3)
    link.add_node(4)

    while link.head.next:
        link.head = link.head.next
        print(link.head.value)


