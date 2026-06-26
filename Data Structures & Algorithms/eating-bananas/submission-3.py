class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2
            hour = 0
            for p in piles:
                hour += math.ceil(p/k)
            if hour > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1
        
        return res