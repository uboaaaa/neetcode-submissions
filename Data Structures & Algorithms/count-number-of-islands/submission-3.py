class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = 0

        def dfs(row, col):
            if (
                row < 0 or
                row >= ROW or
                col < 0 or 
                col >= COL or
                grid[row][col] == '0'
            ):
                return
            
            grid[row][col] = '0'

            for r, c in dirs:
                dfs(row + r, col + c)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res += 1
        
        return res
