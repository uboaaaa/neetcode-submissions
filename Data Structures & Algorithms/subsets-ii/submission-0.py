class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, sub):
            if idx == len(nums):
                res.append(sub[:])
                return

            sub.append(nums[idx])
            dfs(idx + 1, sub)
            sub.pop()
            while idx + 1 < len(nums) and nums[idx +1] == nums[idx]:
                idx += 1
            
            dfs(idx + 1, sub)

        dfs(0, [])
        return res