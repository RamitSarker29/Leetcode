class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        i,j=0,1
        while j<len(nums):
            while nums[j]-nums[i]!=1:
                res.append(nums[i]+1)
                nums[i]=nums[i]+1
            i+=1
            j+=1
        return res
        