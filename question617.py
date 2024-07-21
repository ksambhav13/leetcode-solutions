# [617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)

from typing import Optional

from util import TreeNode, build_tree, display_tree


class Solution:
    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        val1 = root1.val if root1 else 0
        val2 = root2.val if root2 else 0
        node = TreeNode(val1 + val2)
        node.left = self.mergeTrees(
            root1.left if root1 else None, root2.left if root2 else None
        )
        node.right = self.mergeTrees(
            root1.right if root1 else None, root2.right if root2 else None
        )
        return node

    def mergeTrees_non_replacing(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        elif root1 is None:
            return root2
        elif root2 is None:
            return root1
        else:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node


testcases = [
    [1, 3, 2, 5],
    [2, 1, 3, None, 4, None, 7],
    [1],
    [1, 2],
]

for i in range(0, len(testcases), 2):
    display_tree(
        Solution().mergeTrees(build_tree(testcases[i]), build_tree(testcases[i + 1]))
    )
