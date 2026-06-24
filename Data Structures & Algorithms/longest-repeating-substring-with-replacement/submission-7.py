class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        maxf = 0
        hm = {} # char : counts
            
        for i in range(len(s)):
            hm[s[i]] = 1 + hm.get(s[i], 0)
            maxf = max(maxf, hm[s[i]])
            while (i - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
            
            res = max(res, i - l + 1)
        
        return res
            
            

