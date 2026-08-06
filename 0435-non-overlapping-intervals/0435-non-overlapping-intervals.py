class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        end1 = intervals[0][1]
        for start2, end2 in intervals[1:]:
            if start2 < end1:
                count+=1
                end1 = min(end1, end2)
            else:
                end1 = end2
        return count