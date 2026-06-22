class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW, COL = len(board), len(board[0])
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # key: (r//3, c//3)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == '.':
                    continue
                
                if (board[r][c] in rows[r] \
                or board[r][c] in cols[c] \
                or board[r][c] in squares[(r//3, c//3)]):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        
        return True



        
            
        
