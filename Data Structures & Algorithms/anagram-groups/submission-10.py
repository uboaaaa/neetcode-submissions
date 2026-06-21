class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            tuple_key = tuple(key)
            if tuple_key in hm:
                hm[tuple_key].append(s)
            else:
                hm[tuple_key] = [s]
        
        return list(hm.values())
