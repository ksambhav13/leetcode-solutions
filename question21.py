# [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)


from typing import Optional

from util import ListNode, build_linked_list, display_linked_list


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode()
        parent = dummy_head
        while list1 or list2:
            if not list2:
                parent.next = list1
                break
            if not list1:
                parent.next = list2
                break

            if list1.val < list2.val:
                parent.next = list1
                parent = parent.next
                list1 = list1.next
            else:
                parent.next = list2
                parent = parent.next
                list2 = list2.next
        return dummy_head.next


testcases = [
    [1, 2, 4],
    [1, 3, 4],
    [],
    [],
    [],
    [0],
]

for i in range(0, len(testcases), 2):
    display_linked_list(
        Solution().mergeTwoLists(
            build_linked_list(testcases[i]), build_linked_list(testcases[i + 1])
        )
    )
