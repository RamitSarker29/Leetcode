class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        for i in nums:
            curr = max(prev1, i + prev2)
            prev2 = prev1
            prev1 = curr
        return prev1