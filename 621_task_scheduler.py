# [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)


from collections import deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count_map = {}
        for task in tasks:
            task_count_map[task] = task_count_map.get(task, 0) + 1
        heap = [-val for val in task_count_map.values()]
        heapq.heapify(heap)
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                tc = 1 + heapq.heappop(heap)
                if tc < 0:
                    q.append((tc, time + n))
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time


testcases = [
    ["A", "A", "A", "B", "B", "B"],
    2,
    ["A", "C", "A", "B", "D", "B"],
    1,
    ["A", "A", "A", "B", "B", "B"],
    3,
]


for i in range(0, len(testcases), 2):
    print(Solution().leastInterval(testcases[i], testcases[i + 1]))


# A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
