class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Sort the intervals
        sorted_intervals = sorted(intervals, key= lambda x : x[0])
        #Check if first and second interval are overlapping
        prevEnd = sorted_intervals[0][1]
        res = 0
        for start, end in sorted_intervals[1:]:
            if start < prevEnd:
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end
        return res
        

        #if intervals are overlapping remove interval with later endpoint
        #increment counter
        #move to next two intervals