class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]

        for i in range(1, len(nums)):
            if i > max_jump:
                return False
            max_jump = max(max_jump, nums[i] + i)
        
        return True