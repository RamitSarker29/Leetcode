class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_ans = 0
        best_ans = nums[0]
        max_ans = nums[0]
        for i in range(1 , len(nums)) :
            v1 = best_ans + nums[i]
            v2 = nums[i]
            best_ans = max (v1 , v2)
            max_ans = max (max_ans , best_ans)
        return max_ans
        