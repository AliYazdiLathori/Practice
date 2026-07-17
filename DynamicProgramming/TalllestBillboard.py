"""
Idea:
    Use dynamic programming to track the possible height differences between
    the two billboard supports. For each difference, store the maximum possible
    height of the shorter support.

Approach:
    - Maintain a dictionary:
        difference -> maximum smaller support height
    - For each rod, consider two choices:
        1. Add the rod to the taller side:
           - The difference increases by the rod length.
           - The shorter support height stays the same.
        2. Add the rod to the shorter side:
           - The new difference is |difference - rod|.
           - The shorter support height increases by min(difference, rod).
    - After processing all rods, the state with difference 0 represents two
      equal-height supports, so return its stored height.

Topics:
    - Dynamic Programming
    - Hash Map
    - State Compression

Difficulty:
    Hard

Complexity:
    Time Complexity: O(n * S)
        # n = number of rods, S = sum of rod lengths (number of possible differences)

    Space Complexity: O(S)
        # Stores the maximum height for each possible difference
"""
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:

        # difference : maximum smaller support height
        Differences = {0: 0}

        for rod in rods:

            current = Differences.copy()

            for difference, height in current.items():

                # Put rod on the taller side
                new_difference = difference + rod
                Differences[new_difference] = max(
                    Differences.get(new_difference, 0),
                    height
                )

                # Put rod on the shorter side
                new_difference = abs(difference - rod)
                new_height = height + min(difference, rod)

                Differences[new_difference] = max(
                    Differences.get(new_difference, 0),
                    new_height
                )

        return Differences[0]
    
if __name__ == "__main__":
    solution = Solution()
    rods = [1, 2, 3, 6]
    print(solution.tallestBillboard(rods))  # Output: 6