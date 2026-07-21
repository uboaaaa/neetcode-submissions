class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, arr):
        first = 0
        second = 0

        for n in arr:
            curr = max(n + first, second)
            first = second
            second = curr
        
        return second
