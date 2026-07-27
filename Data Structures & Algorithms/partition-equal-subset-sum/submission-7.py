class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for cur_sum in range(target - 1, -1, -1):
                if dp[cur_sum] and cur_sum + num <= target:
                    dp[cur_sum + num] = True

        return dp[-1]