class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 
        part = []

        def dfs(idx):
            if idx >= len(s):
                res.append(part[:])
                return 

            for end in range(idx + 1, len(s) + 1):
                chunk = s[idx:end]
                if chunk == chunk[::-1]:
                    part.append(chunk)
                    dfs(end)
                    part.pop()
        
        dfs(0)
        return res

