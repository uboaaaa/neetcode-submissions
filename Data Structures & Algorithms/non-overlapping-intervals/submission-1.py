class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        res = 0
        safe = intervals[0]

        for i in intervals[1:]:
            if safe[1] <= i[0]:
                safe = i
            else:
                res += 1
        
        return res


