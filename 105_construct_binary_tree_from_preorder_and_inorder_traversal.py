# [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

from util import TreeNode, display_tree
from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if not inorder:
            return None

        root = TreeNode(preorder[0])
        ri = inorder.index(root.val)
        root.left = self.buildTree(preorder[1 : 1 + ri], inorder[0:ri])
        root.right = self.buildTree(preorder[ri + 1 :], inorder[ri + 1 :])
        return root


testcases = [
    [3, 9, 20, 15, 7],
    [9, 3, 15, 20, 7],
    [-1],
    [-1],
]


for i in range(0, len(testcases), 2):
    display_tree(Solution().buildTree(testcases[i], testcases[i + 1]))
