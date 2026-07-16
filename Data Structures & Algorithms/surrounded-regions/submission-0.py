class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        safe = set()

        def dfs(r, c):
            safe.add((r, c))
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                if (
                    0 <= new_r < ROW and
                    0 <= new_c < COL and
                    board[new_r][new_c] == 'O' and
                    (new_r, new_c) not in safe
                ):
                    dfs(new_r, new_c)

        for r in range(ROW):
            for c in range(COL):
                if (
                    r == 0 or
                    c == 0 or
                    r == ROW - 1 or
                    c == COL - 1
                ) and board[r][c] == 'O':
                    dfs(r, c)
        
        for r in range(ROW):
            for c in range(COL):
                if (r, c) not in safe:
                    board[r][c] = 'X'
        
