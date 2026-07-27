class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = set()
        dp.add(0)

        for num in nums:
            nextDP = set()
            for t in dp:
                nextDP.add(t + num)
                nextDP.add(t)
            dp = nextDP
        
        return target in dp
