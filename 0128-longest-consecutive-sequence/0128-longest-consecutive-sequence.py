class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        max_count = 0
        for i in nums :
            count = 1
            first = i
            if first - 1 not in nums :
                while first + 1 in nums :
                    count += 1
                    first += 1
                max_count = max(count , max_count)
        return max_count
            
