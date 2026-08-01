class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum=nums[0]
        max_ans=nums[0]
        min_sum=nums[0]
        min_ans=nums[0]
        total_sum=nums[0]
        for i in range(1,len(nums)):
            total_sum+=nums[i]
            max_sum=max(max_sum+nums[i],nums[i])
            max_ans=max(max_sum,max_ans)
            min_sum=min(min_sum+nums[i],nums[i])
            min_ans=min(min_sum,min_ans)
        return max_ans if max_ans<0 else max(max_ans,total_sum-min_ans)

        