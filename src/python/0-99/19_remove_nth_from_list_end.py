"""
Solution to 19. Remove Nth Node From End of List (https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
Difficulty:     MEDIUM
Runtime:        O(n) - Linear time
Space:          O(1) - Constant space
Submission:     https://leetcode.com/submissions/detail/607704884/
"""
__author__      = "jagwirecode"

from typing import Optional

# Definition for singly-linked list. Defined by Leetcode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of the list.
        Eg. If n is 2, the 2nd from the last node would be removed

        Args:
            head (Optional[ListNode]): Head of list to be traversed
            n (int): Number of nodes from the end of which the node to be removed is located

        Returns:
            Optional[ListNode]: Head of list that has been modified
        """

        # Create dummy node that next points to head to start the left pointer slightly behind.
        # This is so that when the right pointer reaches the end, the left pointer is at the node before the one
        # being removed and not the node itself. This allows for the left.next = left.next.next assignment.
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Keep the right pointer n nodes in front of left, so that when right reaches the end, the left is in pos
        for i in range(0, n):
            right = right.next
        
        # Move pointers along list until right pointer reaches the end
        while right:
            left = left.next
            right = right.next
        
        # Fixes up links between nodes that were connected to the deleted one
        left.next = left.next.next
        
        # Return the head of the linkedlist
        return dummy.next
        
    