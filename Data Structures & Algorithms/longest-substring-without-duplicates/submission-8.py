class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.discard(s[l])
                l += 1
            seen.add(s[r])
            win_len = r - l + 1
            res = max(res, win_len)
        
        return res