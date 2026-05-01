class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            i = 0
            while i < len(intervals):

                # case 1: insert before
                if newInterval[1] < intervals[i][0]:
                    intervals.insert(i, newInterval)
                    return intervals

                # case 2: move forward
                elif newInterval[0] > intervals[i][1]:
                    i += 1

                # case 3: overlap → merge
                else:
                    intervals[i] = [
                        min(newInterval[0], intervals[i][0]),
                        max(newInterval[1], intervals[i][1])
                    ]

                    n = 1
                    while (i + n) < len(intervals) and intervals[i][1] >= intervals[i + n][0]:
                        intervals[i] = [
                            min(intervals[i][0], intervals[i + n][0]),
                            max(intervals[i][1], intervals[i + n][1])
                        ] 
                        del intervals[i + n]
                        

                    return intervals

            # if we finish loop → goes at end
            intervals.append(newInterval)
            return intervals
        