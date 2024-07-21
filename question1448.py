# [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)
from util import TreeNode, build_tree


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count_good_nodes(node: TreeNode | None, max: int):
            if node is None:
                return 0
            count = 0
            if node.val >= max:
                max = node.val
                count += 1
            count += count_good_nodes(node.left, max)
            count += count_good_nodes(node.right, max)
            return count

        count = count_good_nodes(root, root.val)
        return count


testcases = [[3, 1, 4, 3, None, 1, 5], [3, 3, None, 4, 2], [1]]

for testcase in testcases:
    print(Solution().goodNodes(build_tree(testcase)))
