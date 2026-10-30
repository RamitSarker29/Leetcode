class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        hash_map = {0 : 1}
        count = 0
        for i in nums :
            sum += i
            target = sum - k
            if target in hash_map :
                count += hash_map[target]
            if sum in hash_map :
                hash_map[sum] += 1
            else :
                hash_map[sum] = 1
        return count
