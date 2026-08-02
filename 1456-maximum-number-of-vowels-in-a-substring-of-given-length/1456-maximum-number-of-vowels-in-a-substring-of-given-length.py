class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=0
        current_len=0
        max_len=float('-inf')
        for j in range(len(s)):
            if s[j] in 'aeiou':
                current_len+=1
            while j-i+1>k:
                if s[i] in 'aeiou':
                    current_len-=1
                i+=1
            if j-i+1==k:
                max_len=max(max_len,current_len)
        return max_len
                
        