class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for i in intervals:
            curr = res[-1]
            if i[0] <= curr[1]:
                curr[1] = max(curr[1], i[1])
            else:
                res.append(i)
            
            
        return res