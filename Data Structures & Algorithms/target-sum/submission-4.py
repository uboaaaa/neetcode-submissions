class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, curr_sum):
            if i == len(nums):
                return 0 if curr_sum != target else 1
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]

            dp[(i, curr_sum)] = dfs(i + 1, curr_sum + nums[i]) + dfs(i + 1, curr_sum - nums[i])

            return dp[(i, curr_sum)]
        
        return dfs(0, 0)

