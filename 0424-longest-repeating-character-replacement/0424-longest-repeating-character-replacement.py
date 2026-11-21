class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        maxLen = 0
        i , j = 0 , 0
        maxFreq = 0
        for j in range(len(s)) :
            if s[j] in hashMap :
                hashMap[s[j]] += 1
            else :
                hashMap[s[j]] = 1
            maxFreq = max(maxFreq , hashMap[s[j]])
            while (j - i + 1) - maxFreq > k :
                hashMap[s[i]] -= 1
                i += 1
            maxLen = max(j - i + 1 , maxLen)
        return maxLen
                

        