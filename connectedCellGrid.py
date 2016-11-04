class Solution(object):
    def __init__(self):
        self.result = -1
        self.count = 0
        self.moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def solve(self, all_params):
        n, m, grid = all_params
        visited = [[False for j in xrange(m)] for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(m):
                if visited[i][j]==False and grid[i][j] == 1:
                    self.count = 0
                    self.dfs(visited, grid, i, j, n, m)

        return self.result

    def dfs(self, visited, grid, i, j, n, m):
        visited[i][j] = True
        self.count += 1

        for dir in self.moves:
            i1 = i + dir[0]
            j1 = j + dir[1]
            if i1>=0 and i1<n and j1>=0 and j1<m and visited[i1][j1]==False and grid[i1][j1] == 1:
                self.dfs(visited, grid, i1, j1, n, m)

        self.result = max(self.result, self.count)


n = int(raw_input().strip())
m = int(raw_input().strip())
r = 0
grid = []
for grid_i in xrange(n):
    grid_temp = map(int, raw_input().strip().split(' '))
    grid.append(grid_temp)

obj = Solution()
all_params = n, m, grid
r = obj.solve(all_params)

print r