# [133. Clone Graph](https://leetcode.com/problems/clone-graph/)


from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        cloned_nodes = {}

        def clone_graph(node: Optional[Node]):
            if node is None:
                return
            if node.val in cloned_nodes:
                return cloned_nodes[node.val]
            new_node = Node(node.val)
            cloned_nodes[node.val] = new_node
            new_node.neighbors = [clone_graph(nn) for nn in node.neighbors]

            return new_node

        return clone_graph(node)


testcases = [
    [[2, 4], [1, 3], [2, 4], [1, 3]],
    [[]],
    [],
]

# for testcase in testcases:
#     print(Solution().levelOrder(build_tree(testcase)))
