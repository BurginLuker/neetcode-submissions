class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        m = len(grid)
        n = len(grid[0])


        def dfs(row, col):
            if row >= m or col >= n or row < 0 or col < 0:
                return

            if grid[row][col] == '0':
                return

            grid[row][col] = '0'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)

        return islands