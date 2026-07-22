class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum=float('inf')
        for i in range (len(nums)-2):
            j=i+1
            k=len(nums)-1
            while (j<k):
                sum=nums[i]+nums[j]+nums[k]
                if abs(sum-target)<abs(closest_sum-target):
                    closest_sum=sum
                elif sum>target:
                    k-=1
                elif sum<target:
                    j+=1
                else:
                    return sum
        return closest_sum
        