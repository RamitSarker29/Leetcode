class Solution:
    def longestKSubstr(self, s, k):
        # code here
        i=0
        j=0
        hash_map={}
        max_len=0
        for j in range(len(s)):
            if s[j] in hash_map:
                hash_map[s[j]]+=1
            else:
                hash_map[s[j]]=1
            if len(hash_map)==k:
                max_len=max(max_len,j-i+1)
            while len(hash_map)>k:
                hash_map[s[i]]-=1
                if hash_map[s[i]]==0:
                    del hash_map[s[i]]
                i+=1
        return -1 if len(hash_map)<k else max_len
        
