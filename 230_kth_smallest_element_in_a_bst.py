# [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

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
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # def dfs(node, c):
        #     if not node:
        #         return None

        #     res = dfs(node.left, c)
        #     if c[0] == k:
        #         return res
        #     # process node
        #     c[0] += 1
        #     if c[0] == k:
        #         return node.val
        #     return dfs(node.right, c)

        # res = dfs(root, [0])
        # return res
        n = 0
        stack = deque()
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right


testcases = [
    [3, 1, 4, None, 2],
    1,
    [5, 3, 6, 2, 4, None, None, 1],
    3,
]


for i in range(0, len(testcases), 2):
    print(Solution().kthSmallest(build_tree(testcases[i]), testcases[i + 1]))
