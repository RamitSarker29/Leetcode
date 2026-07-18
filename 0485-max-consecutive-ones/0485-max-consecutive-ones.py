class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        max_res=0
        for i in nums:
            if i==1:
                res+=1
                max_res=max(max_res,res)
            else:
                res=0
            
        return max_res
        