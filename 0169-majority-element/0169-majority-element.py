class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hash_map = {}
        for i in nums :
            if i in hash_map :
                hash_map[i] += 1
            else :
                hash_map[i] = 1
        for i in hash_map :
            if hash_map[i] > len(nums) // 2 :
                return i

        