"""
Problem: Maximum Bags With Full Capacity of Rocks
Platform: LeetCode
Difficulty: Medium

Approach:
- Compute the number of rocks needed to fill each bag.
- Store these differences in a list and sort it in ascending order.
- Greedily fill the bags requiring the fewest additional rocks first.
- Continue until the available additional rocks are exhausted.

Time Complexity: O(n log n)
    - O(n) to compute the differences.
    - O(n log n) to sort the differences.
    - O(n) to count the maximum number of full bags.

Space Complexity: O(n)
    - Stores the list of remaining capacities.

Author: Ali
Date: 2026-06-29
address: https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
"""
from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        differentialList = []
        for i in range(len(capacity)):
            differentialList.append(capacity[i]-rocks[i])
        
        differentialList.sort()
        fullBags = 0
        requireStones = 0
        for i in range(len(differentialList)):
            requireStones += differentialList[i]
            if requireStones <= additionalRocks:
                fullBags += 1
            else:
                break

        return fullBags
            
if __name__ == "__main__":
    capacity = [2,3,4,5]
    rocks = [1,2,4,4]
    additionalRocks = 2
    sol = Solution()
    print(sol.maximumBags(capacity, rocks, additionalRocks))