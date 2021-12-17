/**
 * Solution to 189. Rotate Array (https://leetcode.com/problems/rotate-array/)
 * Difficulty: MEDIUM
 * Runtime: O(n)
 * Submission: https://leetcode.com/submissions/detail/602970545/
 *
 * @author jagwirecode
*/

class Solution
{
public:
    // Two pointer technique, reverse and swap in place
    void reverseVec(vector<int> &nums, int left, int right)
    {
        while (left < right)
        {
            swap(nums[left], nums[right]);
            left++;
            right--;
        }
    }

    void rotate(vector<int> &nums, int k)
    {
        int n = nums.size();
        // Safety in case k > n || if k == n
        int rotations = k % n;
        // Reverse whole vector
        reverseVec(nums, 0, n - 1);
        // Reverse first k positions
        reverseVec(nums, 0, rotations - 1);
        // Reverse rest
        reverseVec(nums, rotations, n - 1);
    }

    /**
     * Not in place solution, less efficient and slower
     * 
     * Above solution significantly faster and more memory efficient
    */

    // void rotate(vector<int> &nums, int k)
    // {
    //     int n = nums.size();
    //     vector<int> result(n);

    //     // Loop through vector to calc all new spots
    //     for (int i = 0; i < n; i++)
    //     {
    //         // Calculate new position and account for wrap around
    //         int pos = (i + k) % n;
    //         result[pos] = nums[i];
    //     }

    //     // Copy back into original vector
    //     nums = result;
    // }
};