"""
Solution to 189. Rotate Array (https://leetcode.com/problems/rotate-array/)
Difficulty:     MEDIUM
Runtime:        O(n) - Linear time
Space:          O(1) - Constant space
Submission:     https://leetcode.com/submissions/detail/606253627/
"""
__author__      = "jagwirecode"

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotates array by k in place
        E.g -> [0, 9, 8, 2] with k = 2 -> [8, 2, 0, 9]

        Args:
            nums (List[int]): Array to be rotated
            k (int): Value to rotate array by
        """
        def reverseList(left, right) -> None:
            """
            Reverses partitions of the array and swaps in place.

            Explanation when given the list [3, 99, -1, -100] and k = 2:
            -> Split logic into 3 parts and 2 list segments (one part wraps, the other shifts)
                -> Steps:
                        1. Reverse whole vector
                        -> [-100, -1, 99, 3]
                        2. Reverse the part that wrapped around
                        -> [-1, -100, 99, 3]
                        3. Reverse the part that shifted
                        -> [-1, -100, 3, 99]

            Args:
                left (int): Left pointer used to access the list
                right (int): Right pointer used to access the list
            """
            while(left <= right):
                nums[left], nums[right] = nums[right], nums[left]
                left = left + 1
                right = right - 1
        
        n = len(nums)
        # Safety net if k > n or if k == n
        k = k % n
        
        # Reverse whole array
        reverseList(0, n - 1)
        # Reverse first k positions
        reverseList(0, k - 1)
        # Reverse rest
        reverseList(k, n - 1)
        