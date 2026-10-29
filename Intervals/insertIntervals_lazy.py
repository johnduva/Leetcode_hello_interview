class Solution:
    def insertIntervals_lazy(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            pair1 = intervals[i-1]
            pair2 = intervals[i]
            # If overlap
            if pair1[1] >= pair2[0] and pair1[1] <= pair2[1]:
                intervals[i-1] = [pair1[0], pair2[1]]
                del intervals[i]
            # If "super" overlap (pair1[1] > both nums in pair2)
            elif pair1[1] > pair2[1]:
                del intervals[i]
            else:
                i+=1
        return intervals
