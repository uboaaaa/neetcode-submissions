class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hm = {} # char : counts
            
        for i in range(len(s)):
            hm[s[i]] = 1 + hm.get(s[i], 0)
            dominant = max(hm, key=hm.get)
            while (i - l + 1) - hm[dominant] > k:
                hm[s[l]] -= 1
                dominant = max(hm, key=hm.get)
                l += 1
                
            res = max(res, i - l + 1)
        
        return res
            
            

