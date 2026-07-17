class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num=[]
        for i in nums:
            if i in num:
                i+=1
            else:
                num.append(i)
        nums[:]=num
        return len(nums)