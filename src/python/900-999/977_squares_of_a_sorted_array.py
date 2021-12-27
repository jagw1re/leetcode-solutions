"""
Solution to 977. Squares of a Sorted Array (https://leetcode.com/problems/squares-of-a-sorted-array/)
Difficulty:     EASY
Runtime:        O(n) - Linear time
Space:          O(n) - Linear space
Submission:     https://leetcode.com/submissions/detail/606242169/
"""
__author__      = "jagwirecode"

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Given a list of numbers in ascending order, each element is squared and returned in 
        ascending order

        Args:
            nums (List[int]): Bunch of numbers sorted in ascending order

        Returns:
            List[int]: The original list but with each element squared and sorted ascendingly
        """
        left = 0
        right = index = len(nums) - 1
        result = [None] * len(nums)
        
        # Two pointer technique to sort and square simultaneously
        while(left <= right):
            # If the left side's absolute value is smaller (eg. -4 has an absolute value of 4)
            if(abs(nums[left]) < abs(nums[right])):
                # // Put the squared value into new array and decrement index
                result[index] = nums[right] ** 2
                index = index - 1
                right = right - 1
            else:
                result[index] = nums[left] ** 2
                index = index - 1
                left = left + 1

        return result

# or if you want to cheat and use a python one liner
# class Solution:
#    def sortedSquares(self, nums: List[int]) -> List[int]:
#        return sorted(x * x for x in nums)