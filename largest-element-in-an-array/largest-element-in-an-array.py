class Solution:
    def largestElement(self, nums):
        largest = nums[0]
        for i in range(len(nums)) :
            if largest < nums[i] :
                largest = nums[i]
        return largest
        
