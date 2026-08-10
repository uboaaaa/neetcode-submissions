class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_lastidx_map = {} # char : last seen index
        l = 0
        checkpoint = 0
        res = []

        for i in range(len(s)):
            char_lastidx_map[s[i]] = i

        for end, char in enumerate(s):
            if char in char_lastidx_map:
                checkpoint = max(checkpoint, char_lastidx_map[char])
            
            if end == checkpoint:
                res.append(end - l + 1)
                l = end + 1
        
        return res