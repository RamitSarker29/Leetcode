class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j :
            length = min(height[i] , height[j])
            width = j - i
            area = length * width
            maxArea = max(area , maxArea)
            if length == height[i] :
                i += 1
            else :
                j -= 1
        return maxArea
        

        