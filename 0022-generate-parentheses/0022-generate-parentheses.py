class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def fun(open , close , current):
            if open == close == n :
                ans.append(current)
                return
            if open < n :
                fun(open + 1 , close , current + '(')
            if close < open :
                fun(open , close + 1 , current + ')')
        fun(0 , 0 , '')
        return ans
    
