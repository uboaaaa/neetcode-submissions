class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        prefix, suffix = 0, 0

        for i in range(len(nums)):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[len(nums) - 1 - i] * (suffix or 1)
            res = max(res, prefix, suffix)
        
        return res