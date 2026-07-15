class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dirs = [
            [1, 0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        time = 0
        q = deque()

        def bfs():
            nonlocal time
            while q:
                batch_size = len(q)
                for _ in range(batch_size):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        new_r, new_c = r + dr, c + dc
                        if (
                            0 <= new_r < ROW and
                            0 <= new_c < COL and
                            grid[new_r][new_c] == 1
                        ):
                            grid[new_r][new_c] = 2
                            q.append((new_r, new_c))
                if q: time += 1
                        

        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))

        print(q)        
        bfs()

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    return -1
        
        return time
