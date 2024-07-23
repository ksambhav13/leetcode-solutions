# [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

from typing import List

import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dist = x**2 + y**2
            min_heap.append([dist, x, y])
        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1:])
        return res

    def kClosestManual(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point: List[int]):
            return (point[0] ** 2) + (point[1] ** 2)

        def heapify_up(i):
            print(max_heap[i])

            if i <= 0:
                return
            di = distance(max_heap[i])
            p = (i - 1) // 2
            dp = distance(max_heap[p])
            if dp < di:
                max_heap[p], max_heap[i] = max_heap[i], max_heap[p]
                heapify_up(p)

        def heapify_down(i):
            di = distance(max_heap[i])
            maxi = i
            maxd = di
            if 2 * i + 1 < k:
                dl = distance(max_heap[2 * i + 1])
                if dl > maxd:
                    maxi, maxd = (2 * i + 1), dl
            if 2 * i + 2 < k:
                dr = distance(max_heap[2 * i + 2])
                if dr > maxd:
                    maxi, maxd = (2 * i + 2), dr
            if i != maxi:
                max_heap[i], max_heap[maxi] = max_heap[maxi], max_heap[i]
                heapify_down(maxi)

        max_heap = points[0:k]
        for i in range(k - 1, -1, -1):
            heapify_down(i)
        for point in points[k:]:
            if distance(max_heap[0]) > distance(point):
                max_heap[0] = point
                heapify_down(0)

        return max_heap


testcases = [
    [[1, 3], [-2, 2]],
    1,
    [[3, 3], [5, -1], [-2, 4]],
    2,
    [
        [89, 6],
        [-39, -4],
        [-13, 91],
        [97, -61],
        [1, 7],
        [-66, 69],
        [-51, 68],
        [82, -6],
        [-21, 44],
        [-58, -83],
        [-40, 73],
        [-88, -24],
    ],
    8,
]

for i in range(0, len(testcases), 2):
    print(Solution().kClosest(testcases[i], testcases[i + 1]))
