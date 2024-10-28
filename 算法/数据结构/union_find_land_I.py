class UnionFind:
    def __init__(self, grid):
        m = len(grid)
        n = len(grid[0])
        # 双亲存储任然是一维数组
        self.parents = [-1] * (m * n)
        # 岛屿的数量
        self.count = 0

    def find(self, i):
        root = i
        while self.parents[root] >= 0:
            root = self.parents[root]

        while i != root:
            t = self.parents[i]
            self.parents[i] = root
            i = t

        return root

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx == rooty:
            return
        if self.parents[rooty] > self.parents[rootx]:
            # 累加节点总数
            self.parents[rootx] += self.parents[rooty]
            # 小树合并到大树
            self.parents[rooty] = rootx
        else:
            self.parents[rooty] += self.parents[rootx]
            self.parents[rootx] = rooty
        self.count -= 1

    def get_count(self):
        return self.count

    def set_count(self, x):
        self.count = x



def num_is_lands(grid):
    m = len(grid)
    n = len(grid[0])
    if m <= 0 or n <= 0:
        return 0

    uf = UnionFind(grid)

    # for i in range(m):
    #     for j in range(n):
    #         if grid[i][j] == 1 :
    #             uf.set_count(uf.get_count() + 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 :
                uf.set_count(uf.get_count() + 1)
                # 合并
                if i-1 >= 0 and grid[i-1][j] == 1:
                    uf.union(i*n+j, (i-1)*n+j)
                if i+1 < m and grid[i+1][j] == 1:
                    uf.union(i*n+j, (i+1)*n+j)
                if j-1 >= 0 and grid[i][j-1] == 1:
                    uf.union(i*n+j, i*n+j-1)
                if j+1 < n and grid[i][j+1] == 1:
                    uf.union(i*n+j, i*n+j+1)

    return uf.get_count()


grid = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
count = num_is_lands(grid)
print(count)