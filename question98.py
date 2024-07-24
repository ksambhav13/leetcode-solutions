# [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

from typing import Optional

from util import TreeNode, build_tree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def maxVal(node: Optional[TreeNode]):
            if not node:
                return float("-inf")
            else:
                return max(node.val, maxVal(node.left), maxVal(node.right))

        def minVal(node: Optional[TreeNode]):
            if not node:
                return float("inf")
            else:
                return min(node.val, minVal(node.left), minVal(node.right))

        if not root:
            return True
        return (
            self.isValidBST(root.left)
            and self.isValidBST(root.right)
            and maxVal(root.left) < root.val
            and minVal(root.right) > root.val
        )


testcases = [
    [2, 1, 3],
    [5, 1, 4, None, None, 3, 6],
]

for testcase in testcases:
    print(Solution().isValidBST(build_tree(testcase)))
