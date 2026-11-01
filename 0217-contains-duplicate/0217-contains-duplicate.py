class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_map = {}
        for i in nums :
            if i in hash_map :
                return True
            hash_map[i] = 1
        return False
        