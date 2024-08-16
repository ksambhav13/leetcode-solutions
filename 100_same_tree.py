# [100. Same Tree](https://leetcode.com/problems/same-tree/)

from util import TreeNode, build_tree
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(a, b):
            if a is None and b is None:
                return True
            elif a is None or b is None:
                return False
            elif a.val != b.val:
                return False
            else:
                return dfs(a.left, b.left) and dfs(a.right, b.right)

        return dfs(p, q)


testcases = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2],
    [1, None, 2],
    [1, 2, 1],
    [1, 1, 2],
]


for i in range(0, len(testcases), 2):
    print(Solution().isSameTree(build_tree(testcases[i]), build_tree(testcases[i + 1])))
