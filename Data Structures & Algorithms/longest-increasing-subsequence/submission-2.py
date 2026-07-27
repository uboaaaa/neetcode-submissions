class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        dp = {}

        def dfs(i): # idx -> longest subseq starting from idx
            if i in dp:
                return dp[i]
            
            if i >= len(nums):
                return 0
            
            dp[i] = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], 1 + dfs(j))
            
            return dp[i]
            
        for i in range(len(nums)):
            res = max(res, dfs(i))
        
        return res