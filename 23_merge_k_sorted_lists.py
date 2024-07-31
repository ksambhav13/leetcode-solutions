# [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

from util import ListNode, build_linked_list, display_linked_list
from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, first, second):
        if not second:
            return first
        if not first:
            return second
        if first.val > second.val:
            (first, second) = (second, first)
        #  [[1, 4, 5], [1, 3, 4], [2, 6]],
        cur = first
        prev = None

        while cur and second:
            if cur.val <= second.val:
                prev = cur
                cur = cur.next
            else:
                prev.next = second
                prev = prev.next
                second = second.next
                prev.next = cur

        if second:
            prev.next = second
        return first

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        first = lists[0]

        for i in range(1, len(lists)):
            first = self.merge(first, lists[i])

        return first


testcases = [
    [[1, 4, 5], [1, 3, 4], [2, 6]],
    [],
    [[]],
    [[], []],
    [[], [1, 2, 3]],
]


for testcase in testcases:
    testcase = [build_linked_list(t) for t in testcase]
    display_linked_list(Solution().mergeKLists(testcase))
