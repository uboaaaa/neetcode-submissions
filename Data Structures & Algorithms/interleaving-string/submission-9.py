class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
            
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[-1][-1] = True

        for p1 in range(len(s1), -1, -1):
            for p2 in range(len(s2), -1, -1):
                if p1 < len(s1) and s1[p1] == s3[p1 + p2] and dp[p1 + 1][p2]:
                    dp[p1][p2] = True
                if p2 < len(s2) and s2[p2] == s3[p1 + p2] and dp[p1][p2 + 1]:
                    dp[p1][p2] = True
        
        return dp[0][0]