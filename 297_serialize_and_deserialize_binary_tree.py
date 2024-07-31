# [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

from collections import deque
from util import TreeNode, build_tree, display_tree
from typing import Optional

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def dfs(node):
            res.append(node.val if node else None)
            if node:
                dfs(node.left)
                dfs(node.right)

        res = []
        dfs(root)

        return ",".join([str(i) for i in res])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs():
            if not nodes[self.i]:
                self.i += 1
                return None
            node = nodes[self.i]
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        sdata = data.split(",")
        nodes = []
        for d in sdata:
            if d.isdigit():
                nodes.append(TreeNode(int(d)))
            elif d == "None":
                nodes.append(None)
            else:
                nodes.append(TreeNode(d))
        self.i = 0
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


testcases = [
    # [1, 2, 3, None, None, 4, 5],
    # [],
    [1, 2, 3, None, None, 4, 5, 6, 7],
]


for testcase in testcases:
    ser = Codec()
    deser = Codec()
    # print(ser.serialize(build_tree(testcase)))
    ans = deser.deserialize(ser.serialize(build_tree(testcase)))
    display_tree(ans)
