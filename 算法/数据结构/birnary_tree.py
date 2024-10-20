class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        # 根节点为空
        if not self.root:
            self.root = Node(value)
            return

        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            # 左子树为空
            if not current_node.left:
                current_node.left = Node(value)
                return
            else:
                # 加入到队列
                queue.append(current_node.left)

            # 右子树为空
            if not current_node.right:
                current_node.right = Node(value)
                return
            else:
                queue.append(current_node.right)


def mid(node):
    if not node:
        return
    mid(node.left)
    if node.value:
        print(node.value)
    mid(node.right)


def pre(node):
    if not node:
        return
    if node.value:
        print(node.value)
    pre(node.left)
    pre(node.right)


def post(node):
    if not node:
        return
    post(node.left)
    post(node.right)
    if node.value:
        print(node.value)


def floor(node):
    if not node:
        return
    output = []
    queue = [node]
    while queue:
        current = queue.pop(0)
        # 只访问 结点值不为空
        if current.value:
            output.append(current.value)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return output


def find_sum(node, t):
    flag = False

    def pre(node, value, t):
        nonlocal flag
        if not node:
            return
        sum_a = 0
        if node.value:
            sum_a = node.value + value
            if not node.left and not node.right:
                if t == sum_a:
                    flag = True
        pre(node.left,sum_a if sum_a else value, t)
        pre(node.right, sum_a if sum_a else value, t)

    pre(node, 0, t)
    return flag


if __name__ == '__main__':
    b = BinaryTree()

    # b.add(1)
    # b.add(2)
    # b.add(3)
    # b.add(4)
    # b.add(5)
    # b.add(6)
    # b.add(7)
    # b.add(8)
    # b.add(9)
    # b.add(10)

    b.add(5)
    b.add(4)
    b.add(8)
    b.add(11)
    b.add(None)
    b.add(13)
    b.add(4)
    b.add(7)
    b.add(2)
    b.add(None)
    b.add(None)
    b.add(None)
    b.add(None)
    b.add(None)
    b.add(1)

    # mid(b.root)
    # pre(b.root)
    # post(b.root)

    # print(floor(b.root))

    print(find_sum(b.root, 22))
