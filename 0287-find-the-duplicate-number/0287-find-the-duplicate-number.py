class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[fast]
            fast=nums[fast]
            if slow==fast:
                ptr=0
                while (ptr!=slow):
                    slow=nums[slow]
                    ptr=nums[ptr]
                return ptr