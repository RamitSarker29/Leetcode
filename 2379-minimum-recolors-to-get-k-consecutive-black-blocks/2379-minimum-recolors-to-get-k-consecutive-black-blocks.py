class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i,j=0,k-1
        min_len=float('inf')
        hash_map={}
        for j in range(len(blocks)):
            if blocks[j] in hash_map:
                hash_map[blocks[j]]+=1
            else:
                hash_map[blocks[j]]=1
            if (j-i+1==k):
                min_len=min(min_len,hash_map.get('W',0))
                hash_map[blocks[i]]-=1
                i+=1
        return min_len
