class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i=k-1
        vowel={'a','e','i','o','u'}
        count=0
        max_count=0
        for i in range(k):
            if s[i] in vowel:
                count+=1
                max_count=max(count,max_count)
        for i in range(k,len(s)):
            if s[i] in vowel:
                count+=1
            if s[i-k] in vowel:
                count-=1
            max_count=max(count,max_count)
        return max_count
        