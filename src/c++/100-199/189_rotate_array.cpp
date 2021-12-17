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

    /**
     * Logic to this when given the vector [3, 99, -1, -100] and k = 2.
     * Split logic into 3 parts and 2 vector segments (one part wraps, the other shifts)
     * Steps:
        1. Reverse whole vector
        -> [-100, -1, 99, 3]
        2. Reverse the part that wrapped around
        -> [-1, -100, 99, 3]
        3. Reverse the part that shifted
        -> [-1, -100, 3, 99]
    */
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