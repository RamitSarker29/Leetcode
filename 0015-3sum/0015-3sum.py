class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)) :
            if i > 0 and nums[i] == nums[i - 1] :
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k :
                currentSum = nums[i] + nums[j] + nums[k]
                if currentSum > 0 :
                    k -= 1
                elif currentSum < 0 :
                    j += 1
                else :
                    ans.append([nums[i] , nums[j] , nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1] :
                        j += 1
        return ans


                
            


        