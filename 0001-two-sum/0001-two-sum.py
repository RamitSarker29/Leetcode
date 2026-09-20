class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i , n in enumerate(nums) :
            diff = target - n
            if diff in hash_map :
                return [i , hash_map[diff]]
            else :
                hash_map[n] = i



        