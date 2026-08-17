class Solution:
    def countFreq(self, arr, target):
        # code here
        first = -1
        last = -1
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) //2
            if arr[mid] > target:
                high = mid - 1
            if arr[mid] < target:
                low = mid + 1
            if arr[mid] == target:
                first = mid
                high = mid - 1
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) //2
            if arr[mid] > target:
                high = mid - 1
            if arr[mid] < target:
                low = mid + 1
            if arr[mid] == target:
                last = mid
                low = mid + 1
        return 0 if first == -1 and last == -1 else last - first + 1
