# LeetCode 740. Delete and Earn
# Difficulty: Medium
#
# Problem: Given an array nums, you can pick any nums[i] and earn nums[i]
# points, but doing so deletes every element equal to nums[i]-1 and
# nums[i]+1 from the array. Repeat until no elements remain. Return the
# maximum points you can earn.
#
# Approach: Reduce to House Robber (LC 198). First, bucket the total
# "earnings" per distinct value: cost[v] = v * (count of v in nums).
# Sort the distinct values. Since picking a value forbids its immediate
# neighbors (v-1 and v+1), consecutive values behave exactly like
# adjacent houses you can't both rob. When there's a gap of more than 1
# between two consecutive sorted values, insert a 0 to break the
# adjacency link (so rob() doesn't treat them as neighbors). Then just
# run House Robber on the resulting earnings sequence.
#
# Time complexity: O(n log n) - dominated by sorting the distinct values
# Space complexity: O(n) - cost dict, keys/values lists, new_values list

from typing import List


class Solution:

    # LeetCode 198. House Robber
    # Difficulty: Easy
    #
    # Classic DP: at each index, either skip it (best through i-1) or
    # take it (best through i-2, plus nums[i]). Used here as a helper
    # for deleteAndEarn once values are bucketed into an earnings array.
    def rob(self, nums: List[int]) -> int:
        stackMoney = [0] * len(nums)

        stackMoney[0] = nums[0]  # one house: rob it

        if len(nums) == 1:
            return stackMoney[0]

        stackMoney[1] = max(nums[0], nums[1])  # two houses: take the bigger

        if len(nums) == 2:
            return stackMoney[1]

        for i in range(2, len(nums)):
            # skip house i, or rob it (+ best through i-2)
            stackMoney[i] = max(
                stackMoney[i - 1],
                stackMoney[i - 2] + nums[i]
            )

        return stackMoney[-1]

    def deleteAndEarn(self, nums):
        cost = {}

        # Bucket total points per distinct value: picking value `num`
        # earns `num` points each time it appears.
        for num in nums:
            if num in cost:
                cost[num] = cost[num] + num
            else:
                cost[num] = num

        # Sort distinct values descending (order just needs to be
        # consistent so neighbors in the dict are neighbors in value)
        sorted_cost = dict(sorted(cost.items(), reverse=True))

        keys = list(sorted_cost.keys())
        values = list(sorted_cost.values())

        new_values = []

        for i in range(len(keys)):
            new_values.append(values[i])

            if i < len(keys) - 1:
                # If the next value isn't immediately adjacent (gap > 1),
                # insert a 0 "spacer" so House Robber doesn't treat
                # these two values as forbidden neighbors.
                if keys[i] - keys[i + 1] != 1:
                    new_values.append(0)

        return self.rob(new_values)


if __name__ == "__main__":
    solution = Solution()
    print(solution.deleteAndEarn([3, 3, 3, 4, 2]))