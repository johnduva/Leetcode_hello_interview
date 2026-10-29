class Solution:
    def insertIntervals_onePass(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        i = 0
        n = len(intervals)
      
        # While there's no overlap...
        while i<n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i+=1
          
        # While there *is* an overlap...
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+=1
        output.append(newInterval)

        # No more overlap
        for j in range(i, n):
            output.append(intervals[j])
        
        return output
