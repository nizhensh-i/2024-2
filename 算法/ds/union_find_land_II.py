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

    def set_parent(self, i, val):
        self.parents[i] = val

def num_is_lands(m, n, positions):
    if m <= 0 or n <= 0:
        return []

    ans = []
    grid = [[0 for _ in range(n)] for _ in range(m)]
    uf = UnionFind(grid)

    for i in range(len(positions)):
        position = positions[i]
        grid[position[0]][position[1]] = 1
        # 下标值为陆地的内容不用指向自己的序号
        # uf.set_parent(position[0]*n+position[1], position[0]*n+position[1])
        uf.set_count(uf.get_count()+1)

        if position[0]-1 >= 0 and grid[position[0]-1][position[1]] == 1:
            uf.union(position[0]*n+position[1],(position[0]-1)*n+position[1])

        if position[0]+1 < m and grid[position[0]+1][position[1]] == 1:
            uf.union(position[0]*n+position[1],(position[0]+1)*n+position[1])

        if position[1]-1 >= 0 and grid[position[0]][position[1]-1] == 1:
            uf.union(position[0]*n+position[1],position[0]*n+position[1]-1)

        if position[1]+1 < n and grid[position[0]][position[1]+1] == 1:
            uf.union(position[0]*n+position[1],position[0]*n+position[1]+1)

        ans.append(uf.get_count())
    return ans

m = 3
n = 3
positions = [[0,0],[0,1],[1,2],[2,1]]
ans = num_is_lands(m,n,positions)
print(ans)