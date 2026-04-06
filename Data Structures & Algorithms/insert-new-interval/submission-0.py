class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #initialize result list
        result = []
        i = 0
        #while loop to add all intervals that begin before new interval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        #while loop to merge all overlapping intervals
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        result.append(newInterval)
        #while loop to add all intervals after
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result
