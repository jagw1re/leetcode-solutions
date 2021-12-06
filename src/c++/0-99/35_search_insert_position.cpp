/**
 * Solution to 35. Search Insert Position (https://leetcode.com/problems/search-insert-position/)
 * Difficulty: EASY
 * Runtime: O(log n)
 * Submission: https://leetcode.com/submissions/detail/597709327/
 *
 * @author jagwirecode
*/

class Solution
{
public:
    int searchInsert(vector<int> &nums, int target)
    {
        int size = nums.size();

        // Bounds check
        if (size < 1)
        {
            return 0;
        }

        int low = 0;
        int high = size - 1;
        int mid;
        int index = 0;

        // Begin binary search
        while (low <= high)
        {
            // Safely calculate midpoint
            mid = low + ((high - low) / 2);

            // Lower half check - update where index should be if not present (always 1 more than final midpoint)
            if (nums.at(mid) < target)
            {
                low = mid + 1;
                index = mid + 1;
            }
            // Upper half check
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

        // Return where it should have been if it were present
        return index;
    }
};