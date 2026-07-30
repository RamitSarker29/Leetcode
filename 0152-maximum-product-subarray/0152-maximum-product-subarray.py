class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        i=0
        min_ans=nums[0]
        max_ans=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            v1=nums[i]
            v2=min_ans*nums[i]
            v3=max_ans*nums[i]
            min_ans=min(v1,min(v2,v3))
            max_ans=max(v1,max(v2,v3))
            ans=max(ans,max(min_ans,max_ans))
        return ans

        