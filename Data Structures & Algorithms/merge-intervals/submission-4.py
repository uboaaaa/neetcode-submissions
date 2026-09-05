class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            latest_interval_end = res[-1][1]
            if start <= latest_interval_end:
                res[-1][1] = max(end, latest_interval_end)
            else:
                res.append([start, end])
        
        return res
                
