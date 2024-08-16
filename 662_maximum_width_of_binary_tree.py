# [662. Maximum Width of Binary Tree](https://leetcode.com/problems/maximum-width-of-binary-tree/)

from collections import deque
from util import TreeNode, build_tree
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 1))
        max_w = 1
        while q:
            (node, i) = q.popleft()
            start_p = 0
            cur_w = 0
            for _ in range(len(q)):
                if node:
                    if not start_p:
                        start_p = i
                    else:
                        cur_w = i - start_p
                    q.append((node.left, 2 * i))
                    q.append((node.right, 2 * i + 1))
            if max_w < cur_w:
                max_w = cur_w
        return max_w


testcases = [
    [1, 3, 2, 5, 3, None, 9],
    # [1, 3, 2, 5, None, None, 9, 6, None, 7],
    [1, 3, 2, 5],
    [1, 2, 3, 4, 5],
    [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        None,
        None,
        None,
        1,
        None,
        None,
        None,
        None,
        2,
        2,
        2,
        2,
        2,
        2,
        2,
        None,
        2,
        None,
        None,
        2,
        None,
        2,
    ],
]


for testcase in testcases:
    print(Solution().widthOfBinaryTree(build_tree(testcase)))
