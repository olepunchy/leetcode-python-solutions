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
        # Tracking variables that start at the head node
        current = previous = head

        # While current has a next pointer
        while current.next:
            # Increase size by 1
            size += 1
            # Step current forward by one node
            current = current.next

            # If the size is greater than n + 1
            if size > n + 1:
                # Step previous forward to the next node
                previous = previous.next

        # If size is the same as n
        if size == n:
            return head.next

        else:
            # Point previous two nodes forward
            previous.next = previous.next.next
            return head
