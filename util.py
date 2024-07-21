from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(arr: list[int], i: int = 0) -> Optional[TreeNode]:
    n = len(arr)
    root = None
    if i < n and arr[i] is not None:
        root = TreeNode(arr[i])
        root.left = build_tree(arr, 2 * i + 1)
        root.right = build_tree(arr, 2 * i + 2)
    return root


def normalize_tree(root: Optional[TreeNode]) -> list[int]:
    if not root:
        return []
    res = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            res.append(node.val)
            if node.left or node.right:
                queue.append(node.left)
                queue.append(node.right)
        else:
            res.append(None)
    return res


def display_tree(root: Optional[TreeNode]) -> None:
    print(normalize_tree(root))
