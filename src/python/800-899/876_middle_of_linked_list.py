"""
Solution to 876. Middle of Linked List (https://leetcode.com/problems/reverse-words-in-a-string-iii/)
Difficulty:     EASY
Runtime:        O(n) - Linear time
Space:          O(1) - Constant space
Submission:     https://leetcode.com/submissions/detail/607688323/
"""
__author__      = "jagwirecode"

from typing import Optional

# Definition for singly-linked list. Defined by LeetCode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle (or second middle for odd lengths) node in a linked list and returns it

        Args:
            head (Optional[ListNode]): Head of linked list to traverse

        Returns:
            Optional[ListNode]: Identified middle of linked list
        """

        # Use two pointer technique with slow and fast pointers
        slow = fast = head
        
        # Move fast pointer twice as fast as slow pointer such that when the fast pointer reaches the end,
        # the slow pointer has reached the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow