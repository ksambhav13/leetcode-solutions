# [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

from typing import Optional

from util import ListNode, build_linked_list


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sp, fp = head, head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
            if sp == fp:
                return True
        return False


testcases = [
    [3, 2, 0, -4],
    1,
    [1, 2],
    0,
    [1],
    -1,
]


def connect_tail(head: Optional[ListNode], pos: int):
    if pos < 0:
        return
    i = 0
    p = None
    tail = head
    while tail.next:
        if i == pos:
            p = tail
        i += 1
        tail = tail.next
    tail.next = p


for i in range(0, len(testcases), 2):
    ll = build_linked_list(testcases[i])
    connect_tail(ll, testcases[i + 1])
    print(Solution().hasCycle(ll))
