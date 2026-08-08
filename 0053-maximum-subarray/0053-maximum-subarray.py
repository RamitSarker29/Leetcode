class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        best_sum = nums[0]
        max_sum = nums[0]
        for i in range(1,len(nums)):
            v1 = best_sum +nums[i]
            v2 = nums[i]
            best_sum = max(v1,v2)
            max_sum = max(max_sum,best_sum)
        return max_sum