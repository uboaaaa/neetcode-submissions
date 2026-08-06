class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset = sum(nums)
        print(offset)
        print(target)
        if offset < target:
            return 0

        remap = 2 * offset + 1 
        dp = [[0] * remap for _ in range(len(nums) + 1)]
        dp[0][offset] = 1

        for i in range(1, len(nums) + 1):
            curr_num = nums[i - 1]
            for s in range(remap):
                if dp[i - 1][s] > 0:
                    dp[i][s + curr_num] += dp[i - 1][s]
                    dp[i][s - curr_num] += dp[i - 1][s]
        
        return dp[-1][target + offset]
