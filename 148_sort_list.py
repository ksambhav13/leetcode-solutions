# [148. Sort List](https://leetcode.com/problems/sort-list/)

from util import ListNode, build_linked_list, display_linked_list
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head
        right = self.get_mid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def get_mid(self, node: Optional[ListNode]):
        # display_linked_list(node)
        sp, fp = node, node.next

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        return sp

    def merge(self, left, right):
        first = ListNode(float("-infinity"), None)
        node = first
        while left or right:
            if left and right:
                if left.val <= right.val:
                    node.next = left
                    left = left.next
                else:
                    node.next = right
                    right = right.next
            elif left:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next

        return first.next

    def sortListInsertion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        firstNode = ListNode(0, None)
        node = head
        while node:
            prev, cur = firstNode, firstNode.next
            while cur and cur.val < node.val:
                prev = cur
                cur = cur.next

            next_node = node.next
            node.next = prev.next
            prev.next = node
            node = next_node

        return firstNode.next


testcases = [
    [4, 2, 1, 3],
    [-1, 5, 3, 4, 0],
    [],
]


for testcase in testcases:
    display_linked_list(Solution().sortListInsertion(build_linked_list(testcase)))
