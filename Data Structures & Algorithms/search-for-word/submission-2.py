class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()

        ROW, COL = len(board), len(board[0])

        def dfs(idx, row, col):
            if idx == len(word):
                return True
            if row < 0 or row >= ROW or col < 0 or col >= COL:
                return False
            if (row, col) in seen or board[row][col] != word[idx]:
                return False

            seen.add((row, col))
            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for r, c in dirs:
                if dfs(idx + 1, row + r, col + c):
                    return True
            seen.discard((row, col))

        for i in range(ROW):
            for j in range(COL):
                if dfs(0, i, j):
                    return True

        return False
