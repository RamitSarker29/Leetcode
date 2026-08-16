class Solution:
    def findCeil(self, arr, x):
        # code here
        low = 0
        high = len(arr) - 1
        ans = -1
        while high >= low :
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            if arr[mid] < x:
                low = mid + 1
        return ans

