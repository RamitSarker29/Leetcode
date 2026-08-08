class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            answer[i]*= prefix
            prefix *= nums[i]
        for j in range(len(nums)-1,-1,-1):
            answer[j]*=suffix
            suffix *= nums[j]
        return answer
    
