# Problem: Check if the middle element in the array is unique.

# Idea:
# Find the middle index of the array and count how many times
# the middle element appears in the whole array.
# If it appears more than once, it is not unique; otherwise it is unique.

# Approach:
# 1. Identify the middle index (n // 2).
# 2. Traverse the array and count occurrences of nums[middle].
# 3. Return False if count > 1, else return True.

# Topics:
# Array, Counting, Simulation

# Difficulty: Easy

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        count = 0
        middle = len(nums) // 2
        for i in range(len(nums)):
            if nums[i] == nums[middle]:
                count += 1
        if count > 1:
            return False
        return True

if __name__ == "__main__":
    # Example 1
    nums = [1, 2, 3, 4, 5]
    print(Solution().isMiddleElementUnique(nums))  # Output: True

    # Example 2
    nums = [1, 2, 3, 2, 5]
    print(Solution().isMiddleElementUnique(nums))  # Output: False

    # Example 3
    nums = [1, 1, 1]
    print(Solution().isMiddleElementUnique(nums))  # Output: False