# Idea:
# Maintain the maximum valid left element for each position.
# For every index i (starting from k), the left partner can only
# come from indices <= i - k. Instead of checking all candidates,
# track the maximum valid value in maxLeft and update the best sum.
#
# Topics:
# Array, Prefix Maximum, Greedy, Sliding Window (variant)
#
# Difficulity: Medium
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        maxLeft = nums[0]
        maximumPair = maxLeft + nums[k]
        for i in range(k, len(nums)):
            maxLeft = max(maxLeft, nums[i-k])
            maximumPair = max(maximumPair,maxLeft+nums[i])
        return maximumPair
    

if __name__ == "__main__":
    # Example 1
    nums = [1, 2, 3, 4, 5]
    k = 2
    print(Solution().maxValidPairSum(nums, k))  # Output: 9

    # Example 2
    nums = [10, 20, 30, 40, 50]
    k = 3
    print(Solution().maxValidPairSum(nums, k))  # Output: 90

    # Example 3
    nums = [5, 1, 2, 3, 4]
    k = 1
    print(Solution().maxValidPairSum(nums, k))  # Output: 9