/**
 * Solution to 704. Binary Search (https://leetcode.com/problems/binary-search/)
 * Difficulty: EASY
 * Runtime: O(log n)
 * Submission: https://leetcode.com/submissions/detail/597687066/
 * 
 * @author jagwirecode
*/

class Solution
{
public:
    int search(vector<int> &nums, int target)
    {
        int size = nums.size();

        // Check size is of at least 1
        if (size < 1)
        {
            return -1;
        }

        int low = 0;
        int high = size - 1;
        int mid;

        // Keep looping until left hand side and right hand side are the same
        while (low <= high)
        {
            mid = (low + high) / 2;

            // Check left side
            if (nums.at(mid) < target)
            {
                low = mid + 1;
            }
            // Check right side
            else if (nums.at(mid) > target)
            {
                high = mid - 1;
            }
            // Element found
            else
            {
                return mid;
            }
        }

        // Element not found, return -1
        return -1;
    }
};