class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} # num : idx
        for idx, val in enumerate(nums):
            if target - val in hm:
                return [hm[target - val], idx]
            hm[val] = idx

