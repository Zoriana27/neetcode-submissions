"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda i: i.start)
        heap = [intervals[0].end]
        size = 1
        for meeting in intervals[1:]:
            if meeting.start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, meeting.end)
            size = max(size, len(heap))
        return size
            

        