import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hash_map = {}
        heap = []
        for i in nums :
            if i in hash_map :
                hash_map[i] += 1
            else :
                hash_map[i] = 1
        for i in hash_map :
            heapq.heappush(heap , [hash_map[i] , i])
            if len(heap) > k :
                heapq.heappop(heap)
        return [i[1] for i in heap]
        
        