class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack =[]
        res = [-1] * len(nums)
        nums2 = nums+nums
        for i in range(len(nums2)):
            while stack and nums[stack[-1]] < nums2[i]:
                prev = stack.pop()
                res[prev] = nums2[i]
            if i<len(nums):
                stack.append(i)
        return res
