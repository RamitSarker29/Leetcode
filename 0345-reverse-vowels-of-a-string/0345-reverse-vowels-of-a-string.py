class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        i=0
        j=len(s)-1
        while (i<j):
            if s[i] not in "aeiouAEIOU":
                i+=1
            elif s[j] not in "aeiouAEIOU":
                j-=1
            else:
                s[i],s[j]=s[j],s[i]
                i+=1
                j-=1
        return "".join(s)
