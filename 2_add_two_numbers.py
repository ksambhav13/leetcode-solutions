# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

from util import ListNode, build_linked_list, display_linked_list
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        remainder = 0
        snode = ListNode(0)
        node = snode
        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + remainder
            remainder = sum // 10
            val = sum % 10
            node.next = ListNode(val)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if remainder > 0:
            node.next = ListNode(remainder)
        return snode.next


testcases = [
    [2, 4, 3],
    [5, 6, 4],
    [0],
    [0],
    [9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9],
]


for i in range(0, len(testcases), 2):
    display_linked_list(
        Solution().addTwoNumbers(
            build_linked_list(testcases[i]), build_linked_list(testcases[i + 1])
        )
    )
