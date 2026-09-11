class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def fun(n) :
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in dp :
                return dp[n]
            dp[n] = fun(n - 1) + fun(n - 2)
            return dp[n]
        return fun(n)
        