class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = nums[0]

        for curr_position in range(1, len(nums)):
            if curr_position > max_jump:
                return False
            max_jump = max(max_jump, nums[curr_position] + curr_position)
        
        return True