class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_map = {}
        for i in range(len(nums)) :
            if nums[i] in hash_map :
                return True
            else :
                hash_map[nums[i]] = 1
        return False
        