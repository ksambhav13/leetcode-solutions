# [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

from util import ListNode, build_linked_list, display_linked_list
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake_node = ListNode(-1, head)
        ll = fake_node
        while ll.next:
            l = ll.next
            r = l.next
            if not r:
                break
            ll.next = r
            l.next = r.next
            r.next = l
            ll = l

        return fake_node.next


testcases = [
    [1, 2, 3, 4],
    [],
    [1],
]


for testcase in testcases:
    display_linked_list(Solution().swapPairs(build_linked_list(testcase)))
