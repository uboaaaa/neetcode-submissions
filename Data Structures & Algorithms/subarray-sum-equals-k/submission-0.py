class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        cur_sum = 0
        hm = defaultdict(int) # sum -> count
        hm[0] = 1

        for n in nums:
            cur_sum += n
            diff = cur_sum - k
            result += hm.get(diff, 0)
            hm[cur_sum] += 1
        

        return result
