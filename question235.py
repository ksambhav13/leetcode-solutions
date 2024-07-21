# [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)


from util import TreeNode, build_tree


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        a, b = (p, q) if p < q else (q, p)
        if a <= root.val and b >= root.val:
            return root.val
        if a < root.val and b < root.val:
            return self.lowestCommonAncestor(root.left, a, b)
        else:
            return self.lowestCommonAncestor(root.right, a, b)


testcases = [
    [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
    2,
    8,
    [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5],
    2,
    4,
    [2, 1],
    2,
    1,
]

for i in range(0, len(testcases), 3):
    tree = build_tree(testcases[i])
    print(Solution().lowestCommonAncestor(tree, testcases[i + 1], testcases[i + 2]))
