class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start1 = intervals[0][0]
        end1 = intervals[0][1]
        res=[]
        for start2, end2 in intervals[1:]:
            if end1 >= start2:
                end1 = max(end1, end2)
            else:
                res.append([start1,end1])
                start1=start2
                end1=end2
        res.append([start1,end1])
        return res
