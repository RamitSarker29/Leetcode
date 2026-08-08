class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums =set(nums)
        max_count = 0
        for i in nums:
            if i-1 not in nums:
                    first = i
                    while i+1 in nums:
                        i+=1
                    last = i
                    max_count = max(max_count,last-first+1)
        return max_count 
        