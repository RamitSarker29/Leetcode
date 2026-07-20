class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        l=0
        r=n-1
        k=n-1
        while (l<=r):
            if abs(nums[l])>abs(nums[r]):
                res[k]=nums[l]*nums[l]
                l+=1
            else:
                res[k]=nums[r]*nums[r]
                r-=1
            k-=1
        return res

        