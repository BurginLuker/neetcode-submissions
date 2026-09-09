"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ints = sorted(intervals, key=lambda x:x.start)

        prev_end = None
        for interval in ints:
            if prev_end is not None and prev_end > interval.start:
                return False
            prev_end = interval.end

        return True