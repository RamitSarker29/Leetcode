class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        max_len=0
        hash_map={}
        for j in range(len(s)):
            if s[j] in hash_map:
                hash_map[s[j]]+=1
            else:
                hash_map[s[j]]=1
            while hash_map[s[j]]>1:
                hash_map[s[i]]-=1
                if hash_map[s[i]]==0:
                    del hash_map[s[i]]
                i+=1
            max_len=max(max_len,j-i+1)
        return max_len
