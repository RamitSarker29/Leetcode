class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        res=[]
        for i in range(len(nums)):
            if nums[i] not in res:
                res.append(nums[i])
            else:
                if res.count(nums[i])==k:
                    continue
                else:
                    res.append(nums[i])
        return res
        