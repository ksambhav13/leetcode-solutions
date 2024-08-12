# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

from util import ListNode, build_linked_list, display_linked_list
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        i = 0
        node = None
        while cur:
            cur = cur.next
            i += 1
            if i > n:
                node = node.next if node else head
        if not node:
            return head.next
        node.next = node.next.next
        return head


testcases = [
    [1, 2, 3, 4, 5],
    2,
    [1],
    1,
    [1, 2],
    1,
]


for i in range(0, len(testcases), 2):
    display_linked_list(
        Solution().removeNthFromEnd(build_linked_list(testcases[i]), testcases[i + 1])
    )
