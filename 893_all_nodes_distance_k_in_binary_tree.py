# [893. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

from util import TreeNode, build_tree
from typing import List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def search(root, tv):
    if not root:
        return None
    if root.val == tv:
        return root
    return search(root.left, tv) or search(root.right, tv)


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []

        # get all childs with k distance from node
        def retrieve(node, k):
            if not node:
                return
            if k == 0:
                res.append(node.val)
            else:
                retrieve(node.left, k - 1)
                retrieve(node.right, k - 1)

        # search for target and if found in left retrieve from right and vice versa
        def search(node):
            if not node:
                return 0
            if node == target:
                retrieve(node, k)
                return 1
            left = search(node.left)
            right = search(node.right)
            dist = left or right

            if dist:
                if k - dist == 0:
                    res.append(node.val)
                    return
                elif k - dist > 0:
                    if left:
                        retrieve(node.right, k - dist - 1)
                    if right:
                        retrieve(node.left, k - dist - 1)
                return dist + 1
            return 0

        # retrieve(target, k)
        search(root)
        return res


testcases = [
    [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4],
    2,
    2,
    [1],
    1,
    3,
]


for i in range(0, len(testcases), 3):
    root = build_tree(testcases[i])
    target = search(root, testcases[i + 1])
    print(Solution().distanceK(root, target, testcases[i + 2]))
