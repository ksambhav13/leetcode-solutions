# [103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

from collections import deque
from util import TreeNode, build_tree
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        zig = False
        res = []
        while q:
            row = []
            for _ in range(len(q)):
                if zig:
                    t = q.pop()
                else:
                    t = q.popleft()
                if not t:
                    continue
                row.append(t.val)
                q.appendleft(t.left)
                q.appendleft(t.right)
            # print(row, zig)
            # if zig:
            #     row.reverse()
            # print(row)
            zig = not zig
            if row:
                res.append(row)
        return res


testcases = [
    [3, 9, 20, None, None, 15, 7],
    [1],
    [],
]


for testcase in testcases:
    print(Solution().zigzagLevelOrder(build_tree(testcase)))
