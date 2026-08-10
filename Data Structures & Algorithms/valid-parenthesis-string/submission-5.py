class Solution:
    def checkValidString(self, s: str) -> bool:
        low_open_paren, high_open_paren = 0, 0
        # ((**)
        # 
        for i, c in enumerate(s):
            if c == '(':
                low_open_paren += 1
                high_open_paren += 1

            if c == ')':
                low_open_paren -= 1
                high_open_paren -= 1

            if c == '*': # star case
                low_open_paren -= 1
                high_open_paren += 1
            
            if low_open_paren < 0:
                low_open_paren = 0

            if high_open_paren < 0:
                return False
       
        return True if (low_open_paren == 0) else False
                