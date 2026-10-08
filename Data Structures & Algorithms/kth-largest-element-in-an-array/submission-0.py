class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        kth = 0
        while k > 0:
            kth = heapq.heappop_max(nums)
            k -= 1
        return kth

        