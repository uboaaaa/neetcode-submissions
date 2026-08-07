class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        r, c = len(word2) + 1, len(word1) + 1
        dp = [[-1] * c for _ in range(r)]

        for p2 in range(r):
            dp[p2][-1] = len(word2) - p2
        
        for p1 in range(c):
            dp[-1][p1] = len(word1) - p1
        
        for p2 in range(len(word2) - 1, -1, -1):
            for p1 in range(len(word1) - 1, -1, -1):
                if word1[p1] != word2[p2]:
                    dp[p2][p1] = 1 + min(
                        dp[p2 + 1][p1],
                        dp[p2][p1 + 1],
                        dp[p2 + 1][p1 + 1]
                    )
                else:
                    dp[p2][p1] = dp[p2 + 1][p1 + 1]
        
        return dp[0][0]