class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hash_map = {
            '2' : 'abc' , 
            '3' : 'def' , 
            '4' : 'ghi' , 
            '5' : 'jkl' , 
            '6' : 'mno' , 
            '7' : 'pqrs' , 
            '8' : 'tuv' , 
            '9' : 'wxyz'
        }
        ans = []

        def fun(index , current) :
            if index == len(digits):
                ans.append(current)
                return
            for i in hash_map[digits[index]]:
                fun(index + 1 , current + i)
        fun(0 , '')
        return ans


        