# [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

from typing import Optional

from util import TreeNode, build_tree


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> tuple[bool, int]:
            if node is None:
                return (True, 0)
            (lb, lh) = dfs(node.left)
            (rb, rh) = dfs(node.right)

            balanced = lb and rb and abs(lh - rh) <= 1
            return (balanced, max(lh, rh) + 1)

        balanced, _ = dfs(root)
        return balanced


testcases = [
    [3, 9, 20, None, None, 15, 7],
    [1, 2, 2, 3, 3, None, None, 4, 4],
    [],
]

for testcase in testcases:
    print(Solution().isBalanced(build_tree(testcase)))
