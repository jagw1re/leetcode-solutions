/**
 * Solution to 977. Squares of a Sorted Array (https://leetcode.com/problems/squares-of-a-sorted-array/)
 * Difficulty: EASY
 * Runtime: O(n)
 * Submission: https://leetcode.com/submissions/detail/602931158/
 *
 * @author jagwirecode
*/

class Solution
{
public:
    vector<int> sortedSquares(vector<int> &nums)
    {
        int length = nums.size();
        int index = length - 1;
        int left = 0;
        int right = length - 1;

        vector<int> result(length, 0);

        // Two pointers technique to sort and square at the same time
        while (right >= left)
        {
            // If the left side's absolute value is smaller (eg. -4 has an absolute value of 4)
            if (abs(nums[left]) < abs(nums[right]))
            {
                // Put the squared value into new array and decrement index
                result[index] = nums[right] * nums[right];
                index--;
                right--;
            }
            // Otherwise right side is smaller
            else
            {
                result[index] = nums[left] * nums[left];
                index--;
                left++;
            }
        }
        return result;
    }
};
