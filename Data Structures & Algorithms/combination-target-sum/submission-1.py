class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, sublist):
            if idx == len(nums) or sum(sublist) > target: return
            if sum(sublist) == target: 
                res.append(sublist[:])
                return

            # choices: can either repeat current num, can skip current num, can append current num
            sublist.append(nums[idx])
            dfs(idx, sublist)
            sublist.pop()
            dfs(idx + 1, sublist)

        
        dfs(0, [])
        return res