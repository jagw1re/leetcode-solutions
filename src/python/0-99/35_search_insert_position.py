"""
Solution to 35. Search Insert Position (https://leetcode.com/problems/search-insert-position/)
Difficulty:     EASY
Runtime:        O(log n) - Logarithmic time
Space:          O(1) - Constant space
Submission:     https://leetcode.com/submissions/detail/605862436/
"""
__author__      = "jagwirecode"

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Searches for the target, returns the index if found, otherwise returns the index of where
        the target should be if it were inserted.

        Args:
            nums (List[int]): List of distinct, sorted ascendingly, integers
            target [int]: Number who's index is to be identified
        
        Returns:
            [int]: Index of the number in the list, or where it would be if not currently present
        """    
        low = 0
        high = len(nums) - 1
        mid = 0
        index = 0
        
        # Binary search method
        while(low <= high):
            mid = low + ((high - low) // 2)
            
            if(nums[mid] < target):
                low = index = mid + 1
            elif(nums[mid] > target):
                high = mid - 1
            else:
                return mid
            
        return index
     