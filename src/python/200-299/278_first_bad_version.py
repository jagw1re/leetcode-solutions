"""
Solution to 278. First Bad Version (https://leetcode.com/problems/first-bad-version/)
Difficulty:     EASY
Runtime:        O(log n) - Logarithmic time
Space:          O(1) - Constant space
Submission:     https://leetcode.com/submissions/detail/605856972/
"""
__author__      = "jagwirecode"

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        Identifies the first bad version in n versions

        Args:
            n [int]: Number of versions 

        Returns:
            firstBad [int]: First bad version identified
        """
        if(n == 1):
            return 1
        
        low = 0
        high = n
        mid = 0
        firstBad = -1
        
        # Implement binary search
        while(low <= high):
            mid = low + ((high - low) // 2)
            
            if(isBadVersion(mid) == False):
                low = mid + 1
            else:
                high = mid - 1
                firstBad = mid
            
        return firstBad
   