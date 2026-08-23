import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        hash_map = {}
        ans = []
        for i in s:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        for i in hash_map:
            heapq.heappush(heap, [-hash_map[i], i])
        while len(ans) < len(s):
            current = heapq.heappop(heap)
            if not ans or ans[-1] != current[1]:
                ans.append(current[1])
                current[0] += 1
                if current[0] != 0:
                    heapq.heappush(heap, current)
            else:
                if not heap:
                    return ""
                other = heapq.heappop(heap)
                ans.append(other[1])
                other[0] += 1
                if other[0] != 0:
                    heapq.heappush(heap, other)
                heapq.heappush(heap, current)
        return ''.join(ans)