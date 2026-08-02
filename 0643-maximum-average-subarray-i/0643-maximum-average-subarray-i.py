class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=k-1
        sum=0
        current_avg=0
        res=float('-inf')
        for j in range(len(nums)):
            sum+=nums[j]
            while j-i+1>k:
                sum-=nums[i]
                i+=1
            if j-i+1==k:
                current_avg=sum/k
                res=max(res,current_avg)
        return res



            
        