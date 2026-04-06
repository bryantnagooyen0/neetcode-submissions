class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])

        prevEnd = sorted_intervals[0][1]
        res = 0

        for start,end in sorted_intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                prevEnd = min(prevEnd, end)
                res += 1
        return res
