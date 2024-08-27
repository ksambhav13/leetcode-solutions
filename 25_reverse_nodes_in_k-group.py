# [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

from util import ListNode, build_linked_list, display_linked_list
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = None
        cur = head
        start = dummy
        i = 0
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            i += 1
            if i % k == 0:
                tmp = start.next
                start.next = prev
                start = tmp
                start.next = cur

        cur = prev
        prev = None
        while prev != start.next:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return dummy.next


# None -> 11 -> 10  <- 7

testcases = [
    # [1, 2, 3, 4, 5, 6, 7],
    # 2,
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    4,
    [1, 2, 3, 4],
    4,
]


for i in range(0, len(testcases), 2):
    display_linked_list(
        Solution().reverseKGroup(build_linked_list(testcases[i]), testcases[i + 1])
    )
