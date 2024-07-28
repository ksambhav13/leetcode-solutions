# [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        q = deque()
        q.append((root, 1))

        while q:
            (node, h) = q.popleft()
            if not node:
                continue
            if len(result) < h:
                result.append(node.val)
            if node.right:
                q.append((node.right, h + 1))
            if node.left:
                q.append((node.left, h + 1))

        return result


testcases = [
    [1, 2, 3, 4],
    [1, 2, 3, None, 5, None, 4],
    [1, None, 3],
    [],
]


for testcase in testcases:
    print(Solution().rightSideView(build_tree(testcase)))
