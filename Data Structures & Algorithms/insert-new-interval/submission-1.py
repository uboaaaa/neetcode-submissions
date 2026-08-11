class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            curr = intervals[i]
            if newInterval[1] < curr[0]: # new -> i
                res.append(newInterval)
                return res + intervals[i:]
            if curr[1] < newInterval[0]: # i -> new
                res.append(curr)
            else: # i <= new <= i + 1, conflict case
                newInterval[0] = min(curr[0], newInterval[0])
                newInterval[1] = max(curr[1], newInterval[1])
        res.append(newInterval)
        return res
            





