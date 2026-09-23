class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        current_prefix = strs[0]
        j = len(current_prefix) - 1
        for i in range(1 , len(strs)) :
            while strs[i].startswith(current_prefix) != True :
                j -= 1
                current_prefix = current_prefix[ : j + 1]
        return current_prefix
        
        