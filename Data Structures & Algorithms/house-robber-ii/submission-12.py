class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        first = nums[:-1]
        second = nums[1:]
        dpf, dps = {}, {}

        def dfs(i, arr, dp):
            if i >= len(arr):
                return 0
            
            if i in dp:
                return dp[i]
            
            res = max(arr[i] + dfs(i + 2, arr, dp), dfs(i + 1, arr, dp))
            dp[i] = res
            return dp[i]

        return max(dfs(0, first, dpf), dfs(0, second, dps))