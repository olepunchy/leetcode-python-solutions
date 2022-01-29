"""
Description:

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
----------

Input: head = [1,2,3,4,5]
Output: [3,4,5]

Explanation: The middle node of the list is node 3.


Example 2:
----------

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Fast and Slow approach to solution
        slow = fast = head

        # When traversing the list with a pointer named slow, make another
        # pointer named fast that traverses twice as fast.
        # When fast reaches the end of the list, slow must be the middle.
        while fast and fast.next:
            # Move slow to the next node
            slow = slow.next
            # Move fast foward by two nodes
            fast = fast.next.next

        return slow


class Solution2:
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Put every node into a list in order. The middle node is found
        # by integer division of the list length // 2.
        node_list = [head]

        # Put every node into the list
        while node_list[-1].next:
            node_list.append(node_list[-1].next)

        # Return the middle index of the list
        return node_list[len(node_list) // 2]
