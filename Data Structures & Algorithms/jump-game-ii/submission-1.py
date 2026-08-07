class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        max_reach = 0
        curr_jump_end = 0

        for i in range(len(nums)-1):
            max_reach = max(max_reach, nums[i] + i)
            if i == curr_jump_end:
                jumps += 1
                curr_jump_end = max_reach
        
        return jumps


