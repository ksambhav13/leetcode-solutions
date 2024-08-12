# [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

from util import TreeNode, build_tree
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            nonlocal max_sum
            # if node and (not node.left) and (not node.right):
            #     return node.val
            if not node:
                return 0
            lsum = max(dfs(node.left), 0)
            rsum = max(dfs(node.right), 0)
            print((lsum, rsum))
            max_sum = max(max_sum, lsum + rsum + node.val)
            return node.val + max(lsum, rsum)

        max_sum = root.val
        dfs(root)
        return max_sum


testcases = [
    [1, 2, 3],
    # [-10, 9, 20, None, None, 15, 7],
    # [-3],
    # [1, -2, -3, 1, 3, -2, None, -1],
    # [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
]


for testcase in testcases:
    print(Solution().maxPathSum(build_tree(testcase)))


#                 5
#         4               8
#     11              13      4
# 7       2                       1
