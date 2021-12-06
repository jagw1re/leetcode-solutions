/**
 * Solution to 278. First Bad Version (https://leetcode.com/problems/first-bad-version/)
 * Difficulty: EASY
 * Runtime: O(log n)
 * Submission: https://leetcode.com/submissions/detail/597700277/
 *
 * @author jagwirecode
*/

// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution
{
public:
    int firstBadVersion(int n)
    {
        // Bounds check
        if (n == 1)
        {
            return 1;
        }

        int low = 1;
        int high = n;
        int mid;
        int firstBad = -1;
        bool isBad;

        // Begin binary search
        while (low <= high)
        {
            // Midpoint of binary search
            mid = low + ((high - low) / 2);

            isBad = isBadVersion(mid);

            // If false, move to next potential bad version
            if (isBad == false)
            {
                low = mid + 1;
            }
            // Found bad version, check there are none before it
            else
            {
                high = mid - 1;
                firstBad = mid;
            }
        }

        // Return the first bad version found
        return firstBad;
    }
};