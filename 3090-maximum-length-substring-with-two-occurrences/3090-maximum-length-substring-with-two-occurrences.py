class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        i,j = 0, 0
        hash_map = {}
        for j in range(len(s)):
            if s[j] in hash_map:
                hash_map[s[j]] +=1
            else:
                hash_map[s[j]] = 1
            while hash_map[s[j]] > 2:
                hash_map[s[i]] -=1
                i+=1
            max_len = max(max_len, j-i+1)
        return max_len
