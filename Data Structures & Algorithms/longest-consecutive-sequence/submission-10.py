class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        seen = set(nums)

        for n in nums:
            if n - 1 in seen:
                continue

            curr_max = 0
            curr = n
            while curr in seen:
                curr_max += 1
                curr += 1
            result = max(result, curr_max)
        


        return result

        
        
