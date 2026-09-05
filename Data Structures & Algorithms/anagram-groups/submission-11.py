class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list) # anagram : [words]
        for word in strs:
            idx = str(sorted(word))
            hm[idx].append(word)
        
        return list(hm.values())
            
