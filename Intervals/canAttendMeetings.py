class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        i = 0
        while i < len(intervals)-1:
            pair = intervals[i]
            if pair[1] > intervals[i+1][0]:
                return False
            i+=1
        return True
