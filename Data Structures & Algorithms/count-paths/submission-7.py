class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dirs = [[0, 1], [1, 0]]
        res = 0
        dp = {} #(r, c) : int

        def dfs(r, c): 
            nonlocal res
            if (r, c) in dp:
                return dp[(r, c)]
            if r == m - 1 and c == n - 1:
                return 1
            if r >= m or c >= n or r < 0 or c < 0:
                return 0
            
            dp[(r, c)] = 0
            for dr, dc in dirs:
                dp[(r, c)] += dfs(r + dr, c + dc)

            return dp[(r, c)]
        
        return dfs(0, 0)