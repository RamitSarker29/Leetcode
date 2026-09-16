class Solution:
    def secondLargestElement(self, nums):
        largest1 = nums[0]
        largest2 = -1
        for i in range(len(nums)) :
            if nums[i] > largest1 :
                largest2 = largest1
                largest1 = nums[i]
            if nums[i] > largest2 and nums[i] < largest1 :
                largest2 = nums[i]
        return largest2
        
