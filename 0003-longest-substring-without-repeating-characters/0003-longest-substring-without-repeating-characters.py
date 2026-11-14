class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        count = 0
        hashMap = {}
        i = 0
        j = 0
        for j in range(len(s)) :
            if s[j] in hashMap :
                hashMap[s[j]] += 1
            else :
                hashMap[s[j]] = 1
            while hashMap[s[j]] > 1 :
                hashMap[s[i]] -= 1
                i += 1
            count = j - i + 1
            maxCount = max(count , maxCount)
        return maxCount
            
        