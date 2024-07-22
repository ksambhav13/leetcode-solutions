# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

from typing import Optional

from util import TreeNode, build_tree


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)
        return max(lh, rh) + 1


testcases = [
    [3, 9, 20, None, None, 15, 7],
    [1, None, 2],
]

for testcase in testcases:
    print(Solution().maxDepth(build_tree(testcase)))
