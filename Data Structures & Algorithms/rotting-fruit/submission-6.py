class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW_RANGE, COL_RANGE = range(len(grid)), range(len(grid[0]))
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = deque()
        fresh = 0
        time = 0

        for r in ROW_RANGE:
            for c in COL_RANGE:
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while fresh > 0 and q:
            batch_size = len(q)

            for _ in range(batch_size):
                r, c = q.popleft()
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc
                    if (
                        new_r in ROW_RANGE and
                        new_c in COL_RANGE and
                        grid[new_r][new_c] == 1
                    ):
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        q.append((new_r, new_c))
            
            time += 1
        
        return -1 if fresh else time
        
