class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        visited = set()
        for u, v, w in times:
            edges[u].append((w, v))

        minHeap = [(0, k)]
        
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            t = max(t, w1)
            visited.add(n1)
            for w2, n2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1+w2, n2))

        return t if len(visited) == n else -1


        