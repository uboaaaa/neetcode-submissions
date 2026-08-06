class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        def dfs(p1, p2):
            if p1 == len(s1) and p2 == len(s2):
                return True 
            if dp[p1][p2] != -1:
                return dp[p1][p2]
            
            path1, path2 = False, False
            if p1 < len(s1) and s1[p1] == s3[p1 + p2]:
                path1 = dfs(p1 + 1, p2)
            if p2 < len(s2) and s2[p2] == s3[p1 + p2]:
                path2 = dfs(p1, p2 + 1)
            
            dp[p1][p2] = path1 or path2
            return dp[p1][p2]
        
        return dfs(0, 0)

            
