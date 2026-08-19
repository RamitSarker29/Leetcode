class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        row = -1
        while low <= high:
            mid = (low + high) //2
            if matrix[mid][-1] < target:
                low = mid + 1
            if matrix[mid][-1] > target:
                row = mid
                high = mid - 1
            if matrix[mid][-1] == target:
                return True
        if row == -1:
            return False
        low = 0
        high = len(matrix[row]) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] < target:
                low = mid + 1
            if matrix[row][mid] > target:
                high = mid - 1
            if matrix[row][mid] == target:
                return True
        return False


