class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        positive = 0
        negative = 0
        while low <= high :
            mid = (low + high) //2
            if nums[mid] >= 0 :
                high = mid - 1
            else :
                low = mid + 1
        negative = low
        low = 0
        high = len(nums) - 1
        positive = 0
        while low <= high :
            mid = (low + high) //2
            if nums[mid] > 0 :
                high = mid - 1
            else :
                low = mid + 1
        positive = len(nums) - low
        return max(positive , negative)
        