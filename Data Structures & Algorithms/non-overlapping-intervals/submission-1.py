class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        print(intervals)
        end = intervals[0][1]
        remove = 0

        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr[0] < end:
                remove += 1
            else:
                end = max(end, curr[1])


        return remove