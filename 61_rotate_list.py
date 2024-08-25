# [61. Rotate List](https://leetcode.com/problems/rotate-list/)

from util import ListNode, build_linked_list, display_linked_list
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        l = 1
        tail = head
        while tail.next:
            l += 1
            tail = tail.next
        k = k % l
        if k == 0:
            return head
        node = head
        for i in range(l - k - 1):
            node = node.next

        h = node.next
        node.next = None
        tail.next = head
        return h


testcases = [
    [1, 2, 3, 4, 5],
    5,
    [0, 1, 2],
    4,
    [1, 2],
    5,
]


for i in range(0, len(testcases), 2):
    display_linked_list(
        Solution().rotateRight(build_linked_list(testcases[i]), testcases[i + 1])
    )
