class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        hash_map = {0:1}
        for i in nums:
            sum +=i
            need = sum -k
            if need in hash_map:
                count +=hash_map[need]
            if sum in hash_map:
                hash_map[sum] +=1
            else:
                hash_map[sum]=1
        return count 

