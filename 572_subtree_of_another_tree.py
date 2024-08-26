# [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

from util import TreeNode, build_tree
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_equal(node, subnode):
            if node and subnode:
                if node.val != subnode.val:
                    return False
                return is_equal(node.left, subnode.left) and is_equal(
                    node.right, subnode.right
                )

            elif node or subnode:
                return False
            else:
                return True

        def search(node):
            if not node:
                return False
            if node.val == subRoot.val:
                res = is_equal(node, subRoot)
                if res:
                    return True
            return search(node.left) or search(node.right)

        return search(root)


testcases = [
    [3, 4, 5, 1, 2],
    [4, 1, 2],
    [3, 4, 5, 1, 2, None, None, None, None, 0],
    [4, 1, 2],
]


for i in range(0, len(testcases), 2):
    print(Solution().isSubtree(build_tree(testcases[i]), build_tree(testcases[i + 1])))
