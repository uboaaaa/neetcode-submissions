class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # s = "foobar" , wordDict = "bar", "foo"
        dp = {} # s index -> bool

        def dfs(i): # idx -> bool
            if i >= len(s):
                return True
            if i in dp:
                return dp[i]

            for word in wordDict:
                end = i + len(word)
                if s[i:end] == word and dfs(end):
                    dp[i] = True
                    return dp[i]
            dp[i] = False
            return dp[i]

        return dfs(0)