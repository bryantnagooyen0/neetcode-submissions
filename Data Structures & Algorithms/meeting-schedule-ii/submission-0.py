"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #get start times in an array and sort
        sorted_start = sorted([i.start for i in intervals])
        #get end times in an array and sort
        sorted_end = sorted([i.end for i in intervals])

        s, e = 0, 0
        count = 0
        res = 0

        while s < len(sorted_start):
            if sorted_start[s] < sorted_end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1

            res = max(count, res)
        return res
                
        