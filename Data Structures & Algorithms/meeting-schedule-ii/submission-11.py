"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        sp, ep = 0, 0
        curr = 0
        res = -1
        # 0, 5, 15
        # 10, 20, 40
        while sp < len(starts):
            if starts[sp] < ends[ep]:
                sp += 1
                curr += 1
            elif starts[sp] >= ends[ep]:
                ep += 1
                curr -= 1
            res = max(res, curr)

        return res