class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == []:
            return True
        
        if s2 == []:
            return False
        
        s1_freq = collections.Counter(s1)
        s2_freq = {}
        l = 0 

        for r in range(len(s2)):
            s2_freq[s2[r]] = 1 + s2_freq.get(s2[r], 0)
            print(s2_freq.items())
            while (r - l + 1) == len(s1):
                if s2_freq == s1_freq:
                    return True
                s2_freq[s2[l]] -= 1
                if s2_freq[s2[l]] == 0:
                    del s2_freq[s2[l]]
                l += 1



        
        return False

        
