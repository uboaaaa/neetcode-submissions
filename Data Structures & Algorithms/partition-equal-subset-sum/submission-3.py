class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2 
        dp = {} # (idx, cur_sum) -> bool

        def dfs(i, cur_sum): # (idx, cur_sum) -> bool
            nonlocal target
            if (i, cur_sum) in dp:
                return dp[(i, cur_sum)]
            if i >= len(nums) or cur_sum > target:
                return False
            if cur_sum == target:
                return True
            
            dp[(i, cur_sum)] = dfs(i + 1, cur_sum) or dfs(i + 1, cur_sum + nums[i])
            return dp[(i, cur_sum)]

        return dfs(0, 0)            
