class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min, res = nums[0], nums[0], nums[0]

        for n in nums[1:]:
            cur_max, cur_min = max(n, n * cur_max, n * cur_min), min(n, n * cur_max, n * cur_min)
            res = max(res, cur_max)
        
        return res