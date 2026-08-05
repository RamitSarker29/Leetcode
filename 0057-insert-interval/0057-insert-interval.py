class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        res = []
        ans = []
        inserted = False
        for start, end in intervals:
            if not inserted and newInterval[0] <= start:
                res.append(newInterval)
                inserted = True
            res.append([start, end])
        if not inserted:
            res.append(newInterval)
        res.sort()
        start1, end1 = res[0]
        for start2, end2 in res[1:]:
            if end1 >= start2:
                end1 = max(end1, end2)
            else:
                ans.append([start1, end1])
                start1, end1 = start2, end2
        ans.append([start1, end1])
        return ans