class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i , n in enumerate(nums) :
            seen = target - n
            if seen in hash_map :
                return ([hash_map[seen] , i])
            else :
                hash_map[n] = i
            
        