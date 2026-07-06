class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        sub = []

        def dfs(sub):
            nonlocal seen
            if len(sub) == len(nums):
                res.append(sub[:])
                return
            
            for num in nums:
                if num in seen: continue
                
                sub.append(num)
                seen.add(num)
                dfs(sub)
                sub.pop()
                seen.discard(num)
        
        dfs(sub)
        return res