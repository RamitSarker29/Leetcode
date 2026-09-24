class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = 0
        current_sum = 0
        for i in range(n + 1) :
            total_sum += i
        for j in nums :
            current_sum += j
        return total_sum - current_sum
        