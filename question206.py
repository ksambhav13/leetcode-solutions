# [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

from typing import Optional
from util import ListNode, build_linked_list, display_linked_list


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev


testcases = [
    [1, 2, 3, 4, 5],
    [1, 2],
    [],
]

for testcase in testcases:
    display_linked_list(Solution().reverseList(build_linked_list(testcase)))
