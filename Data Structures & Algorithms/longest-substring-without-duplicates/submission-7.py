class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        hm = {}
        res = 0
        l = 0
        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            while hm[s[r]] > 1:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        
        return res
        
