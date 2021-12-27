"""
Solution to 704. Binary Search (https://leetcode.com/problems/binary-search/)
Difficulty:     EASY
Runtime:        O(log n) - Logarithmic time
Space:          O(1) - Constant space
Submission:     https://leetcode.com/submissions/detail/605815910/
"""
__author__      = "jagwirecode"

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Performs binary search on nums in search for target

        Args:
            nums (List[int]): List of numbers sorted ascendingly to be searched through
            target [int]: The number being searched for

        Returns:
            [int]: Index of target or -1 if not present
        """
        low = 0;
        high = len(nums) - 1;
        mid = -1

        # Two pointer binary search approach         
        while(low <= high):
            mid = low + ((high - low) // 2)
            
            if(nums[mid] < target):
                low = mid + 1
            elif(nums[mid] > target):
                high = mid - 1
            else:
                return mid
            
        return -1