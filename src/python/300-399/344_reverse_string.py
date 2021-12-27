"""
Solution to 344. Reverse String (https://leetcode.com/problems/reverse-string/)
Difficulty:     EASY
Runtime:        O(n) - Linear time
Space:          O(1) - Constant space
Submission:     https://leetcode.com/submissions/detail/606910941/
"""
__author__      = "jagwirecode"

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverses an input string (in the form of a list of string chars for some reason) in-place

        Args:
            s (List[str]): String (list of chars) to be reversed

        Returns:
            List[str]: Modified list of chars that is now reversed
        """
        left = 0
        right = len(s) - 1
        
        # Two pointer technique, swap in place from start and end
        while(left <= right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
        return s

# Can also cheat with a one liner 
# class Solution:
    # def reverseString(self, s: List[str]) -> None:
        # s.reverse()
        # return s
        