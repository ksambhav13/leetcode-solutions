# [113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)

from util import TreeNode, build_tree
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, last_sum, cur: List[int]):
            if not node:
                return
            cur.append(node.val)
            cur_sum = last_sum + node.val
            if cur_sum == targetSum and (not node.left) and (not node.right):
                res.append(cur[:])
            else:
                dfs(node.left, cur_sum, cur)
                dfs(node.right, cur_sum, cur)
            cur.pop()

        dfs(root, 0, [])
        return res


testcases = [
    [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
    22,
    [1, 2, 3],
    5,
    [1, 2],
    0,
    [1, -2, -3, 1, 3, -2, None, -1],
    -1,
]


for i in range(0, len(testcases), 2):
    print(Solution().pathSum(build_tree(testcases[i]), testcases[i + 1]))
