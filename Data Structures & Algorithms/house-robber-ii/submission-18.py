class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))

    def helper(self, arr):
        if len(arr) <= 1:
            return arr[0]

        first = arr[0]
        second = max(arr[0], arr[1])

        for i in range(2, len(arr)):
            curr = max(arr[i] + first, second)
            first = second
            second = curr
        
        return second
