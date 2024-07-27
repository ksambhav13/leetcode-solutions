# [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)


from typing import Optional
from util import TreeNode, build_tree


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right


testcases = [
    # [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
    # 5,
    # 0,
    [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
    5,
    4,
    # [1, 2],
    # 1,
    # 2,
]

for i in range(0, len(testcases), 3):
    tree = build_tree(testcases[i])

    def find(tree: Optional[TreeNode], val) -> Optional[TreeNode]:
        if not tree:
            return None
        if tree.val == val:
            return tree
        return find(tree.left, val) or find(tree.right, val)

    print(
        Solution()
        .lowestCommonAncestor(
            tree, find(tree, testcases[i + 1]), find(tree, testcases[i + 2])
        )
        .val
    )
