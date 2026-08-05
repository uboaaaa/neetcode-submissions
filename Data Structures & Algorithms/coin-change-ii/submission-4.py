class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]

        def dfs(c, a):
            if a < 0 or c == len(coins):
                return 0
            if a == 0:
                return 1
            if dp[c][a] != -1:
                return dp[c][a]

            dp[c][a] = dfs(c, a - coins[c]) + dfs(c + 1, a)
            
            return dp[c][a]
        
        return dfs(0, amount)