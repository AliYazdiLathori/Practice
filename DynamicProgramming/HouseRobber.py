# LeetCode 198. House Robber
# Difficulty: Medium
#
# Problem: Given an array of non-negative integers representing money
# stashed in houses along a street, find the maximum amount you can rob
# without robbing two adjacent houses.
#
# Approach: Dynamic programming (bottom-up). At each house i, you either
# skip it (keep the best total through i-1) or rob it (best total through
# i-2, plus nums[i]). Take whichever is larger.
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])
#
# Time complexity: O(n) - single pass through the array
# Space complexity: O(n) - dp array of size len(nums)
#                    (could be optimized to O(1) with two variables)

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        stackMoney = [0] * len(nums)
        stackMoney[0] = nums[0]  # only one house: rob it
        if len(nums) == 1:
            return stackMoney[0]
        stackMoney[1] = max(nums[0], nums[1])  # two houses: take the bigger one
        if len(nums) == 2:
            return stackMoney[1]
        for i in range(1, len(nums)):
            # best so far = either skip house i (stackMoney[i-1])
            # or rob house i + best through i-2 (stackMoney[i-2] + nums[i])
            stackMoney[i] = max(stackMoney[i-1], stackMoney[i-2]+nums[i])

        return stackMoney[-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.rob([1,2,3,1]))