# [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

from util import ListNode, build_linked_list
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        node = head
        while node is not None:
            stack.append(node.val)
            node = node.next
        node = head
        while node:
            if node.val != stack.pop():
                return False
            node = node.next
        return True


testcases = [
    [1, 2, 2, 1],
    [1, 2],
]


for testcase in testcases:
    print(Solution().isPalindrome(build_linked_list(testcase)))
