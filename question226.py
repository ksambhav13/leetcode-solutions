# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
from typing import Optional

from util import TreeNode, build_tree, display_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root


testcases = [[4, 2, 7, 1, 3, 6, 9], [2, 1, 3], []]
for testcase in testcases:
    # display_tree(build_tree(testcase))
    display_tree(Solution().invertTree(build_tree(testcase)))
