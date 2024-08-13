# [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)

from util import ListNode, build_linked_list, display_linked_list
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        even_start = head.next
        odd = head
        even = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_start

        return head


testcases = [
    [1, 2, 3, 4, 5],
    [2, 1, 3, 5, 6, 4, 7],
]


for testcase in testcases:
    display_linked_list(Solution().oddEvenList(build_linked_list(testcase)))
