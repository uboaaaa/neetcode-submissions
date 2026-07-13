class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        res = 0
        seen = set()

        def dfs(row, col):
            if (
                row < 0 or
                row >= ROW or
                col < 0 or 
                col >= COL or
                (row, col) in seen or
                grid[row][col] == '0'
            ):
                return
            
            seen.add((row, col))

            dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for r, c in dirs:
                dfs(row + r, col + c)

        for i in range(ROW):
            for j in range(COL):
                curr = grid[i][j]
                if (i, j) not in seen and curr == '1':
                    dfs(i, j)
                    res += 1
        
        return res
