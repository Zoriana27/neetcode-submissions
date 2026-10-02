class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(heap)
        while heap:
            if len(heap) == 1:
                return heap[0]
            stone1 = heapq.heappop_max(heap)
            stone2 = heapq.heappop_max(heap)
            if stone1 != stone2:
                heapq.heappush_max(heap, abs(stone1 - stone2))
        return 0
        