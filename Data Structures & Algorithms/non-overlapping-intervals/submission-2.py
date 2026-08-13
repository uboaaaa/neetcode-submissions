class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        res = 0
        last_end_time = intervals[0][1]

        for i in intervals[1:]:
            if i[0] >= last_end_time:
                last_end_time = i[1]
            else:
                res += 1
        
        return res


