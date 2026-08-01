class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=nums[0]
        max_ans=nums[0]
        min_sum=nums[0]
        min_ans=nums[0]
        for i in range(1,len(nums)):
            max_sum=max(max_sum+nums[i],nums[i])
            max_ans=max(max_ans,max_sum)
            min_sum=min(min_sum+nums[i],nums[i])
            min_ans=min(min_sum,min_ans)
        return max(max_ans,abs(min_ans))