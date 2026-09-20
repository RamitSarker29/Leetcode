class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        i = 0
        current_sum = 0
        best_sum = nums[0]
        max_sum = nums[0]
        for i in range(1 , len(nums)) :
            v1 = nums[i]
            v2 = best_sum + nums[i]
            best_sum = max(v1 , v2)
            max_sum = max(best_sum , max_sum)
        return max_sum
        