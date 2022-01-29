"""
Description:

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
----------

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]


Example 2:
----------

Input: head = [1], n = 1
Output: []

Example 3:
----------

Input: head = [1,2], n = 1
Output: [1]

"""
from typing import Optional


class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def remove_nth_from_end(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:

        size = 1
        current = previous = head

        while current.next:
            size += 1
            current = current.next

            if size > n + 1:
                previous = previous.next

        if size == n:
            return head.next

        else:
            previous.next = previous.next.next
            return head
