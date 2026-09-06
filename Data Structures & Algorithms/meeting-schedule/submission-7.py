"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
            
        intervals.sort(key = lambda i: i.start)
        prev_interval_end = intervals[0].end

        for curr_interval in intervals[1:]:
            if curr_interval.start < prev_interval_end:
                return False
            prev_interval_end = curr_interval.end
        
        return True