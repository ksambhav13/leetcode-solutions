# [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)


from typing import Optional

from util import TreeNode, build_tree


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxh = 0

        def h(node):
            nonlocal maxh
            if not node:
                return 0
            ldepth = h(node.left)
            rdepth = h(node.right)
            maxh = max(maxh, ldepth + rdepth)
            if ldepth < rdepth:
                return rdepth + 1
            else:
                return ldepth + 1

        h(root)
        return maxh


testcases = [
    [1, 2, 3, 4, 5],
    [1, 2],
    [2, 3, None, 1],
]

for testcase in testcases:
    print(Solution().diameterOfBinaryTree(build_tree(testcase)))
