import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [[-cnt, 0] for cnt in count.values()]
        heapq.heapify(maxHeap)
        timer = 0
        wait_list = deque()
        while maxHeap or wait_list:
            if wait_list and wait_list[0][1] <= timer:
                heapq.heappush(maxHeap, wait_list.popleft())
            if maxHeap and maxHeap[0][1] <= timer:
                task = heapq.heappop(maxHeap)
                task[0] += 1
                task[1] = 1 + timer + n
                if task[0] < 0:
                    wait_list.append(task)
            timer += 1
        return timer
