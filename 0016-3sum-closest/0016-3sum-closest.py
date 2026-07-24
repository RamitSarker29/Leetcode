class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        closest_sum=float('inf')
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while (j<k):
                current_sum=nums[i]+nums[j]+nums[k]
                if current_sum==target:
                    return current_sum
                elif abs(current_sum-target)<abs(closest_sum-target):
                    closest_sum=current_sum
                elif current_sum>target:
                    k-=1
                elif current_sum<target:
                    j+=1
        return closest_sum

        