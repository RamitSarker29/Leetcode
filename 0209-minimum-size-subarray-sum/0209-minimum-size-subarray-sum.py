class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        min_len=float('inf')
        window_sum=0
        for j in range(len(nums)):
            window_sum+=nums[j]
            while window_sum>=target:
                min_len=min(min_len,j-i+1)
                window_sum-=nums[i]
                i+=1
        return 0 if min_len==float('inf') else min_len