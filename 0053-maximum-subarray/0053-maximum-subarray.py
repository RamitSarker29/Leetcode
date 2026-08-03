class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        best_sum=nums[0]
        ans=nums[0]
        best_sum=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2= best_sum+nums[i]
            best_sum=max(v1,v2)
            ans=max(ans,best_sum)
        return ans
        