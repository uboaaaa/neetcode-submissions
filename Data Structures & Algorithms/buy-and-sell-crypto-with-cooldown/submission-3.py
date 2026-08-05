class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = [[0] * 2 for _ in range(N + 2)]

        for day in range(N - 1, -1, -1):
            # holding (1)
            sell = prices[day] + dp[day + 2][0]
            dp[day][1] = max(sell, dp[day + 1][1])

            # not holding (0)
            buy = -prices[day] + dp[day + 1][1]
            dp[day][0] = max(buy, dp[day + 1][0])
        
        return dp[0][0]
