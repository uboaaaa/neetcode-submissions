class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {} # (day, holding) : profit
    
        def dfs(day, holding):
            if (day, holding) in dp:
                return dp[(day, holding)]
            if day >= len(prices):
                return 0
            
            if holding:
                dp[(day, holding)] = max(prices[day] + dfs(day + 2, False), dfs(day + 1, True))
            else:
                dp[(day, holding)] = max(-prices[day] + dfs(day + 1, True), dfs(day + 1, False))
            
            return dp[(day, holding)]

        
        return dfs(0, False)