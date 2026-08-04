class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen=set(nums)
        res=[]
        min_num=min(nums)
        max_num=max(nums)
        while min_num!=max_num:
            if min_num +1 not in seen:
                res.append(min_num + 1)
            min_num+=1
        return res
