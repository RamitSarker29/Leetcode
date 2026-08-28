class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        if x < 10 :
            return True
        def fun(x) :
            rev = []
            original = x
            while x > 0 :
                d = x % 10
                rev.append(str(d))
                x = x // 10
            rev = ''.join(rev)
            if rev == str(original) :
                return True
            else :
                return False
        return fun(x)

        