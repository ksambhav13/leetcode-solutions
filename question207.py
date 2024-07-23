# [207. Course Schedule](https://leetcode.com/problems/course-schedule/)

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def top_sort(key: int):
            if key in visited:
                return False

            if not dep_map[key]:
                return True

            visited.add(key)
            for dep in dep_map[key]:
                if not top_sort(dep):
                    return False
            visited.remove(key)
            dep_map[key] = []
            return True

        visited = set()
        dep_map: dict[int, List[int]] = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            dep_map[crs].append(pre)

        for key in range(numCourses):
            if not top_sort(key):
                return False
        return True


testcases = [
    2,
    [[1, 0]],
    2,
    [[1, 0], [0, 1]],
    5,
    [[1, 2], [2, 3], [3, 4], [4, 2]],
    5,
    [[1, 2], [2, 4], [4, 3]],
]

for i in range(0, len(testcases), 2):
    print(Solution().canFinish(testcases[i], testcases[i + 1]))
