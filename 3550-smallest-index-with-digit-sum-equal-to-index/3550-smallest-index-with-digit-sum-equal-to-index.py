class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def fun (n) :
            ans = 0
            if n <= 9 :
                return ans + n
            while n > 0 :
                d = n % 10
                ans += d
                n = n // 10
            return ans
        for i in range(len(nums)) :
            digit_sum = fun(nums[i])
            if digit_sum == i :
                return i
        return -1


        


        