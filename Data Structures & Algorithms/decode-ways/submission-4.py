class Solution:
    def numDecodings(self, s: str) -> int:
        first = 1
        second = 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            curr = 0

            if int(s[i]) != 0:
                curr += second
            if 10 <= int(s[i-1:i+1]) <= 26:
                curr += first
            
            first = second
            second = curr
        
        return second
