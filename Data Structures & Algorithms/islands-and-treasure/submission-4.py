class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                if (
                    0 <= new_r < ROW and
                    0 <= new_c < COL and
                    grid[new_r][new_c] == 2147483647 
                ):
                    q.append((new_r, new_c))
                    grid[new_r][new_c] = grid[r][c] + 1

        