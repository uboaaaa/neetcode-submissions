class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(i): # amount -> ways
            if i < 0:
                return float('inf')
            if i == 0:
                return 0
            if i in dp:
                return dp[i]
            
            min_coins = float('inf')
            for c in coins:
                min_coins = min(min_coins, 1 + dfs(i - c))
            
            dp[i] = min_coins
            return dp[i]
        
        ans = dfs(amount)
        return ans if ans != float('inf') else -1
