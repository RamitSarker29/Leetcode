class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        window_sum=0
        max_sum=float('-inf')
        for j in range(len(nums)):
            window_sum+=nums[j]
            while j-i+1>k:
                window_sum-=nums[i]
                i+=1
            if j-i+1==k:
                max_sum=max(max_sum,window_sum)
        return max_sum/k

        