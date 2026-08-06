class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        def dfs(p1, p2):
            if p1 == len(word1): # if we reach the end of word1, tack on remaining
                return len(word2[p2:])
                
            if p2 == len(word2):
                return len(word1[p1:])

            if dp[p1][p2] != 0:
                return dp[p1][p2]
            
            if word1[p1] != word2[p2]:
                dp[p1][p2] = 1 + min(
                    dfs(p1, p2 + 1), # insertion
                    dfs(p1 + 1, p2), # deletion
                    dfs(p1 + 1, p2 + 1) # replace
                )
            else:
                dp[p1][p2] = dfs(p1 + 1, p2 + 1)
            
            return dp[p1][p2]
        
        return dfs(0, 0)
