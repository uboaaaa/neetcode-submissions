class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, sublist, subsum):
            if subsum == target:
                res.append(sublist[:])
                return 
            if idx == len(candidates) or subsum > target: return

            
            sublist.append(candidates[idx])
            subsum += candidates[idx]
            dfs(idx + 1, sublist, subsum)
            sublist.pop()
            subsum -= candidates[idx]

            while idx + 1 < len(candidates) and candidates[idx+1] == candidates[idx]:
                idx += 1
            dfs(idx + 1, sublist, subsum)
        
        dfs(0, [], 0)
        return res