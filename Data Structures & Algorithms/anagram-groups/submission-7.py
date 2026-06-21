class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            # bat tab -> abt
            key = tuple(sorted(s))
            if key in hm:
                hm[key].append(s)
            else:
                hm[key] = [s]
        
        return list(hm.values())