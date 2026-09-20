class Solution:
    def fib(self, n: int) -> int:
        def fun (n) :
            if n == 0 :
                return 0
            if n == 1 :
                return 1
            ans = fun(n-1) + fun(n - 2)
            return ans
        return fun(n)
        