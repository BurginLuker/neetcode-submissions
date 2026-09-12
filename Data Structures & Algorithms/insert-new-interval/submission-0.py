class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []

        for i in range(len(intervals)):
            curr = intervals[i]

            if newInterval[1] < curr[0]:
                out.append(newInterval)
                return out + intervals[i:]
            elif newInterval[0] > curr[1]:
                out.append(curr)
            else:
                newInterval = [min(curr[0], newInterval[0]), max(curr[1], newInterval[1])]

        out.append(newInterval)
        return out