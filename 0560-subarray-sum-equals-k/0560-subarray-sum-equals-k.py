class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash_map = {0 : 1}
        count = 0
        sum = 0
        for i in nums :
            sum += i
            target = sum - k
            if target in hash_map :
                count += hash_map[target]
            hash_map[sum] = hash_map.get(sum , 0) + 1
        return count
            

        