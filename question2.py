# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

from typing import Optional

from util import ListNode, build_linked_list, display_linked_list


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        remainder = 0
        parent_node, head_node = None, None
        while l1 is not None or l2 is not None or remainder > 0:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0
            sum = l1_val + l2_val + remainder
            digit = sum % 10
            remainder = sum // 10
            if head_node is None:
                head_node = parent_node = ListNode(digit)
            else:
                parent_node.next = ListNode(digit)
                parent_node = parent_node.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        return head_node


testcases = [
    [2, 4, 3],
    [5, 6, 4],
    [0],
    [0],
    [9, 9, 9, 9, 9, 9, 9],
    [9, 9, 9, 9],
]
for i in range(0, len(testcases), 2):
    l1 = build_linked_list(testcases[i])
    l2 = build_linked_list(testcases[i + 1])
    display_linked_list(Solution().addTwoNumbers(l1, l2))
