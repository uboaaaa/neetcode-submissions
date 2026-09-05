class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list) # anagram : [words]
        for word in strs:
            idx = [0] * 26
            for c in word:
                idx[ord(c) - ord('a')] += 1
            hm[tuple(idx)].append(word)
        
        return list(hm.values())
            
