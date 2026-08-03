class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        hash_map={0:1}
        res=0
        for i in nums:
            prefix_sum+=i
            ans=prefix_sum-k
            if ans in hash_map:
                res+=hash_map[ans]
            if prefix_sum in hash_map:
                hash_map[prefix_sum]+=1
            else:
                hash_map[prefix_sum]=1
        return res
        