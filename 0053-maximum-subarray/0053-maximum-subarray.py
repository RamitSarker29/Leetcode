class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        ans=nums[0]
        best_ans=nums[0]
        res=float('-inf')
        for i in range(1,len(nums)):
            v1=best_ans+nums[i]
            v2=nums[i]
            best_ans=max(v1,v2)
            ans=max(best_ans,ans)
        return ans
        