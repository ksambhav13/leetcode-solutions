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

    def __repr__(self) -> str:
        return f"val = {self.val}"


def build_tree(arr: list[int]) -> Optional[TreeNode]:
    n = len(arr)
    if n == 0:
        return None
    nodes = [TreeNode(tn) if tn is not None else None for tn in arr]
    root = nodes[0]
    q = deque()
    q.append(root)
    for i in range(1, n - 1, 2):
        pn = q.popleft()
        if nodes[i]:
            pn.left = nodes[i]
            q.append(pn.left)

        if nodes[i + 1]:
            pn.right = nodes[i + 1]
            q.append(pn.right)
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
