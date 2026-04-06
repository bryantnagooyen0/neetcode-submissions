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
        #Sort the intervals by start
        sorted_intervals = sorted(intervals, key = lambda x: x.start)
        #check if intervals are overlapping by checking prevEnd and newStart
        prevEnd = sorted_intervals[0].end

        for interval in sorted_intervals[1:]:
            start, end = interval.start, interval.end
            if prevEnd > start:
                return False
            else:
                prevEnd = end
        return True
