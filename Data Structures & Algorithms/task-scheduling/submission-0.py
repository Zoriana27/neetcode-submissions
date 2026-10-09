class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        cooldownQ = deque() #pairs of [frequency, idleTime] where idleTime is the time at which the task with the corresponding frequency can be processed

        while maxHeap or cooldownQ:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task != 0:
                    cooldownQ.append((task, time + n))
            if cooldownQ and cooldownQ[0][1] == time:
                heapq.heappush(maxHeap, cooldownQ.popleft()[0])
        return time
            
             