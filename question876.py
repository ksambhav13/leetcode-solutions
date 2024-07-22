# [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
from typing import Optional

from util import ListNode, build_linked_list


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sp = head
        fp = head
        while fp is not None and fp.next is not None:
            sp = sp.next
            fp = fp.next.next
        return sp


testcases = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
]

for testcase in testcases:
    print(Solution().middleNode(build_linked_list(testcase)).val)
