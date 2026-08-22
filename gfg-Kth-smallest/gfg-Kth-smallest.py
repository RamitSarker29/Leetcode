import heapq
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        heap = []
        for i in arr :
            heapq.heappush(heap , -i)
            if len(heap) > k:
                heapq.heappop(heap)
        return -heap[0]

