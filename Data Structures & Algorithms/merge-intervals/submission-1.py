class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        start, end = intervals[0][0], intervals[0][1]

        out = []
        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr[0] > end:
                out.append([start, end])
                start = curr[0]

            end = max(end, curr[1])

        out.append([start, end])
        return out

