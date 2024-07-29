# [310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)


from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj_list = defaultdict(list)

        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        edge_count = {}
        leaves = deque()
        for src, neighbours in adj_list.items():
            if len(neighbours) == 1:
                leaves.append(src)
            edge_count[src] = len(neighbours)

        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neighbour in adj_list[node]:
                    edge_count[neighbour] -= 1
                    if edge_count[neighbour] == 1:
                        leaves.append(neighbour)


testcases = [
    4,
    [[1, 0], [1, 2], [1, 3]],
    6,
    [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]],
]


for i in range(0, len(testcases), 2):
    print(Solution().findMinHeightTrees(testcases[i], testcases[i + 1]))
