# [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

from collections import deque
from typing import List, Optional

from util import TreeNode, build_tree


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append((0, root))
        res = []
        cur = 0
        lot = []
        while q:
            (o, node) = q.popleft()
            if node is None:
                continue
            if cur == o:
                lot.append(node.val)
            else:
                res.append(lot)
                cur = o
                lot = [node.val]
            q.append((o + 1, node.left))
            q.append((o + 1, node.right))
        if lot:
            res.append(lot)
        return res


testcases = [
    [3, 9, 20, None, None, 15, 7],
    [1],
    [],
]

for testcase in testcases:
    print(Solution().levelOrder(build_tree(testcase)))
