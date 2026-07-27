class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j=0,0
        hash_map={}
        max_freq=0
        max_len=0
        for j in range(len(s)):
            if s[j] in hash_map:
                hash_map[s[j]]+=1
            else:
                hash_map[s[j]]=1
            max_freq=max(max_freq,hash_map[s[j]])
            while (j-i+1-max_freq>k):
                hash_map[s[i]]-=1
                if hash_map[s[i]]==0:
                    del hash_map[s[i]]
                i+=1
            max_len=max(max_len,j-i+1)
        return max_len   