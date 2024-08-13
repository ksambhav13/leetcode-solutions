# [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)


from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def visit(i):
            if visited[i] == 2:
                return False
            if visited[i] == 1:
                return True
            visited[i] = 1
            depsi = deps[i]
            for di in depsi:
                cyclic = visit(di)
                if cyclic:
                    return True
            topos.append(i)
            visited[i] = 2
            return False

        deps = defaultdict(list)
        visited = [0] * numCourses
        topos = []

        for p in prerequisites:
            deps[p[0]].append(p[1])

        for i in range(numCourses):
            cyclic = visit(i)
            if cyclic:
                return []

        return topos


testcases = [
    2,
    [[1, 0]],
    4,
    [[1, 0], [2, 0], [3, 1], [3, 2]],
    1,
    [],
    2,
    [[0, 1], [1, 0]],
]


for i in range(0, len(testcases), 2):
    print(Solution().findOrder(testcases[i], testcases[i + 1]))
