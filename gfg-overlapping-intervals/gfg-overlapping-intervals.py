class Solution:
    def isIntersect(self, intervals):
       # Code Here
       intervals.sort()
       start1 = intervals[0][0]
       end1 = intervals[0][1]
       for start2, end2 in intervals[1:]:
            if start2 <= end1:
               return True
            start1 = start2
            end1 = end2
       return False
           
             
       
