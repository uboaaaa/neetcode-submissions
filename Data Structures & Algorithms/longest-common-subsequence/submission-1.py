class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * len(text2) for _ in range(len(text1))]

        def dfs(p1, p2):
            if p1 >= len(text1) or p2 >= len(text2):
                return 0

            if dp[p1][p2] != -1:
                return dp[p1][p2]
            
            if text1[p1] == text2[p2]:
                dp[p1][p2] = 1 + dfs(p1 + 1, p2 + 1)
            else:
                dp[p1][p2] = max(dfs(p1 + 1, p2), dfs(p1, p2 + 1))

            return dp[p1][p2]
        
        return dfs(0, 0)