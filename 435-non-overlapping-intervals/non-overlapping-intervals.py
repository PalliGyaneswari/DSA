class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        c=0
        p=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0]<p:
                c+=1
            else:
                p=intervals[i][1]
        return c
        