class UnionFind:
    def __init__(self, grid):
        m = len(grid)
        n = len(grid[0])
        # 双亲存储任然是一维数组
        self.parent = [-1]*(m*n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.parent[i*n +j] = i*n+j
                    
    def find(self, i):
        root = i
        while self.parent[root] >= 0:
            root = self.parent[root]
        
        while i != root:
            t = self.parent[i]
            self.parent[i] = root
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
        
            
        
                    
        