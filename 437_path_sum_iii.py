# [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)

from util import TreeNode, build_tree
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0

        def dfs(node):
            if not node:
                return []
            lchilds = dfs(node.left)
            rchilds = dfs(node.right)
            child_sums = [0] + lchilds + rchilds
            for i in range(len(child_sums)):
                child_sums[i] = node.val + child_sums[i]
                if child_sums[i] == targetSum:
                    self.count += 1
            return child_sums

        dfs(root)
        return self.count


testcases = [
    # [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1],
    # 8,
    # [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1],
    # 22,
    [1, 2, None, -2, None],
    1,
]


for i in range(0, len(testcases), 2):
    print(Solution().pathSum(build_tree(testcases[i]), testcases[i + 1]))
