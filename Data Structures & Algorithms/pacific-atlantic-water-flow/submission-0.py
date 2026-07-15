class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        ROW, COL = len(heights), len(heights[0])

        pacific_set, atlantic_set = set(), set()
        p, a = deque(), deque()

        def bfs(q, res_set):
            while q:
                r, c = q.popleft()
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc
                    if (
                        0 <= new_r < ROW and
                        0 <= new_c < COL and
                        heights[new_r][new_c] >= heights[r][c] and
                        (new_r, new_c) not in res_set
                    ):
                        res_set.add((new_r, new_c))
                        q.append((new_r, new_c))
        
        for r in range(ROW):
            for c in range(COL):
                if r == 0 or c == 0:
                    p.append((r, c))
                    pacific_set.add((r, c))
                if r == ROW - 1 or c == COL - 1:
                    a.append((r, c))
                    atlantic_set.add((r, c))

        bfs(p, pacific_set)
        bfs(a, atlantic_set) 

        return list(pacific_set & atlantic_set)