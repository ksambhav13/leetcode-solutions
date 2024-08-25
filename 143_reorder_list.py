# [143. Reorder List](https://leetcode.com/problems/reorder-list/)

from util import ListNode, build_linked_list, display_linked_list
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second list
        node = slow.next
        prev = None
        slow.next = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        # merge first and second second list
        node = head
        while prev:
            tmp = prev.next
            prev.next = node.next
            node.next = prev
            node = prev.next
            prev = tmp

        return head

    def reorderListStack(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        stack = []
        while slow:
            stack.append(slow)
            slow = slow.next
        node = head
        while len(stack) > 1:
            t = stack.pop()
            t.next = node.next
            node.next = t
            node = t.next
        stack[0].next = None
        return head


testcases = [
    # [1],
    # [1, 2],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
]


for testcase in testcases:
    display_linked_list(Solution().reorderList(build_linked_list(testcase)))
