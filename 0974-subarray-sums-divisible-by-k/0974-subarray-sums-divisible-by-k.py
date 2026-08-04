class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum=0
        hash_map={0:1}
        count=0
        for i in nums:
            sum+=i
            need=sum%k
            if need<0:
                need+=k
            if need in hash_map:
                count+=hash_map[need]
                hash_map[need]+=1
            else:
                hash_map[need]=1
        return count
            
        