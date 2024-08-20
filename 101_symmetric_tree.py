# [101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

from util import TreeNode, build_tree
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left, right):
            if left and right:
                if left.val != right.val:
                    return False
                else:
                    return dfs(left.left, right.right) and dfs(left.right, right.left)
            elif left or right:
                return False
            else:
                return True

        return dfs(root.left, root.right)


testcases = [
    [1, 2, 2, 3, 4, 4, 3],
    [1, 2, 2, None, 3, None, 3],
]


for testcase in testcases:
    print(Solution().isSymmetric(build_tree(testcase)))
