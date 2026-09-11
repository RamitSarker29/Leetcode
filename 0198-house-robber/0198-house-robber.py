class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def fun (n) :
            if n == 0 :
                return nums[0]
            if n == 1 :
                return max (nums[0] , nums[1])
            if n in dp :
                return dp[n]
            dp[n] = max (fun(n - 2) + nums[n] , fun(n - 1))
            return dp[n]
        return fun (len(nums) - 1)
        