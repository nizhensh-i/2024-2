# 集合元素为一维数组

class UnionFind:

    def __init__(self, UFSets:list):
        n = len(UFSets)
        self.parents = [-1]*n

    
    def find(self, i):
        root = i

        # 循环找到根
        while self.parents[root] >= 0:
            root = self.parents[root]

        # 压缩路径
        while i != root:
            # t指向x的父节点
            t = self.parents[i]
            # x直接挂到根节点下
            self.parents[i] = root
            # x指向父节点，开始将父节点都直接挂到根节点下
            i = t
        # 返回根节点编号
        return root

    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 == root2:
            return
        # 根节点为负数
        # root2节点数更少
        if self.parents[root2] > self.parents[root1]:
            # 累加节点总数
            self.parents[root1] += self.parents[root2]
            # 小树合并到大树
            self.parents[root2] = root1
        else:
            self.parents[root2] += self.parents[root1]
            self.parents[root1] = root2

    # def union(self, root1, root2):
    #     if root1 == root2:
    #         return
    #     # 根节点为负数
    #     # root2节点数更少
    #     if self.parents[root2] > self.parents[root1]:
    #         # 累加节点总数
    #         self.parents[root1] += self.parents[root2]
    #         # 小树合并到大树
    #         self.parents[root2] = root1
    #     else:
    #         self.parents[root2] += self.parents[root1]
    #         self.parents[root1] = root2

if __name__ == '__main__':
    # 集合元素数组
    a = [1,2,36,8,9]
    u = UnionFind(a)

    # 对下标1,2元素执行并操作
    u.union(1, 2)

    # 查找下标1元素的所属集合
    root1 = u.find(1)
    # 查找下标2元素的所属集合
    root2 = u.find(2)
    # 查找下标3元素的所属集合
    root3 = u.find(3)
    # 查找下标4元素的所属集合
    root4 = u.find(4)
    print(root1)
    print(root2)
    print(root3)
    print(root4)
