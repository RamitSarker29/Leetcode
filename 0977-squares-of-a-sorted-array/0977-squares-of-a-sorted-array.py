class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        i=0
        j=len(nums)-1
        k=len(nums)-1
        while (i<=j):
            if abs(nums[i])>abs(nums[j]):
                res[k]=nums[i]*nums[i]
                i+=1
            else:
                res[k]=nums[j]*nums[j]
                j-=1
            k-=1
        return res
        