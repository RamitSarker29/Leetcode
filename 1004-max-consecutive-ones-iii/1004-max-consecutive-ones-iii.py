class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        hash_map={}
        max_len=float('-inf')
        for j in range(len(nums)):
            if nums[j] in hash_map:
                hash_map[nums[j]]+=1
            else:
                hash_map[nums[j]]=1
            while hash_map.get(0,0)>k:
                hash_map[nums[i]]-=1
                i+=1
            max_len=max(max_len,j-i+1)
        return max_len
