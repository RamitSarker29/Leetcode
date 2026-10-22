class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [1] * len(nums)
        left_product = 1
        right_product = 1
        for i in range(len(nums)) :
            ans[i] = left_product
            left_product *= nums[i]
        for j in range(len(nums) - 1 , - 1 , - 1) :
            ans[j] *= right_product
            right_product *= nums[j]
        return ans