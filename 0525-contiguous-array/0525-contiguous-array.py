class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero=0
        one=0
        hash_map={}
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            else:
                one+=1
            diff=one-zero
            if diff==0:
                res=max(res,i+1)
                continue
            if diff in hash_map:
                res=max(res,i-hash_map[diff])
            else:
                hash_map[diff]=i
        return res
        