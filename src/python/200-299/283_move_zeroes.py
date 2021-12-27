"""
Solution to 283. Move Zeroes (https://leetcode.com/problems/move-zeroes/)
Difficulty:     EASY
Runtime:        O(n) - Linear time
Space:          O(1) - Constant space
Submission:     https://leetcode.com/submissions/detail/606900916/
"""
__author__      = "jagwirecode"

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all zeroes to end of list whilst maintaining relative order of other elements. Uses constant space
        and therefore in place.

        Args:
            nums (List[int]): List to move all zeroes to the end
        """
        slow = 0
        fast = 0
        
        # Two pointer technique - maintains a slow and fast pointer
        while fast < len(nums):
            # If a non-zero is found, swap it with the last known zero, so the zero is pushed toward the end
            if(nums[fast] != 0):
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1