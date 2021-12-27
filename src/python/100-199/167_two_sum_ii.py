"""
Solution to 167. Two Sum II: Input Array is Sorted (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
Difficulty:     EASY
Runtime:        O(n) - Linear time
Space:          O(1) - Constant space
Submission:     https://leetcode.com/submissions/detail/606910941/
"""
__author__      = "jagwirecode"

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Returns indexes of two array elements that add up to the target

        Args:
            numbers (List[int]): Array of integers, sorted ascendingly
            target (int): Number that two elements should sum to

        Returns:
            List[int]: Indexes of elements that add up to target. Beginning from 1 for some reason (blame the
                       problem spec not me)
        """
        
        left = 0
        right = len(numbers) - 1
        
        """
        Uses two pointer technique:
        As it is sorted, we can move pointers based on if the sum is greater than or less than the target.
            Eg. target is 9 and array contains [0, 4, 5, 6, 8]
                0 + 8 = 8 which is less than 9, so move left pointer up
                4 + 8 = 12 which is greater than 9 so move right pointer down
                4 + 6 = 10 which is again greater, move right down
                4 + 5 = 9 -> target found, return indexes of 4 and 5

        Returns:
            List[int]: Indexes of elements from original list that add to the target
        """
        while(left < right):
            sum = numbers[left] + numbers[right]
            if(sum > target):
                right -= 1
            elif(sum < target):
                 left += 1
            else:
                return [left + 1, right + 1]