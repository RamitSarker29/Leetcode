class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_ans=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            v1=best_ans+nums[i]
            v2=nums[i]
            best_ans=max(v1,v2)
            ans=max(ans,best_ans)
        return ans