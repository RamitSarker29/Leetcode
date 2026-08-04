class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        hash_map={}
        res=[]
        for i in range(len(nums)):
            if nums[i] not in hash_map:
                hash_map[nums[i]]=1
        min_num=min(nums)
        max_num=max(nums)
        while min_num!=max_num:
            if min_num +1 not in hash_map:
                res.append(min_num + 1)
            min_num+=1
        return res
