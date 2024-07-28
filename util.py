from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
            queue.append(node.left)
            queue.append(node.right)
        else:
            res.append(None)
    l = len(res) - 1
    while res[l] is None:
        l -= 1
    return res[: l + 1]


def display_tree(root: Optional[TreeNode]) -> None:
    print(normalize_tree(root))


def build_linked_list(arr: list[int], i: int = 0) -> Optional[ListNode]:
    root, parent = None, None
    for num in arr:
        if root is None:
            root = ListNode(num)
            parent = root
        else:
            parent.next = ListNode(num)
            parent = parent.next
    return root


def display_linked_list(node: Optional[ListNode]) -> None:
    if not node:
        print(node)
        return
    print(node.val, end=" ")
    if node.next:
        print("->", end=" ")
        display_linked_list(node.next)
    else:
        print()
