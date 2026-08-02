class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=k-1
        window_sum=sum(nums[:k])
        max_sum=window_sum
        for j in range(k,len(nums)):
            window_sum+=nums[j]
            window_sum-=nums[i]
            i+=1
            max_sum=max(max_sum,window_sum)
        return max_sum/k

        