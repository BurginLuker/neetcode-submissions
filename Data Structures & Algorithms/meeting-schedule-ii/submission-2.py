"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from queue import PriorityQueue

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key = lambda x:x.start)
        pq = PriorityQueue()

        for i in intervals:
            if pq.empty():
                pq.put(i.end)
            else:
                top = pq.queue[0]
                if i.start < top:
                    pq.put(i.end)
                else:
                    pq.get()
                    pq.put(i.end)

        return pq.qsize()




