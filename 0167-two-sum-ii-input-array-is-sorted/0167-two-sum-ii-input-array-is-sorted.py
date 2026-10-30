class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while i < j :
            currentSum = numbers[i] + numbers[j]
            if currentSum > target :
                j -= 1
            elif currentSum < target :
                i += 1
            else :
                return i + 1 , j + 1

        