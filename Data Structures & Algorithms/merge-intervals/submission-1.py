class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        res = []
        while intervals:
            interval = heapq.heappop(intervals)
            if res:
                curr = res[-1]
                if interval[0] <= curr[1]:
                    curr[1] = max(curr[1], interval[1])
                else:
                    res.append(interval)
            else:
                res.append(interval)
            
        return res