class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = 1 
        for num in nums:
            if num - 1 in nums:
                continue
            
            curr = num
            subres = 1
            while curr + 1 in nums:
                subres += 1
                curr += 1

            res = max(res, subres)

        return res