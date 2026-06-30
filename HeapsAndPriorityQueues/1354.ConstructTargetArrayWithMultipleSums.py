"""
Problem: Construct Target Array With Multiple Sums
Platform: LeetCode
Difficulty: Hard

Approach:
This solution works in reverse using a max-heap to simulate the construction process.

Instead of building the target array from [1, 1, ..., 1], we repeatedly reduce the largest element by treating it as the result of previous sum operations. At each step, we:

- Extract the largest element using a max heap.
- Compute the sum of the remaining elements.
- Replace the largest element with its previous value using modulo operation (largest % rest).
- Continue until all elements become 1 (valid case) or an invalid state is detected.

Key Idea:
Work backwards from the target array using a greedy strategy with a max heap, ensuring each step preserves validity of the construction process.

Time Complexity: O(n log n * k), where k is number of reduction steps
Space Complexity: O(n)
"""
import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)
        while True:
            largest = -heapq.heappop(heap)
            rest = total - largest
            if largest == 1 or rest == 1:
                return True 
            if rest == 0:
                return False
                
            replacedNum = largest % rest
            
            if rest > largest or replacedNum < 1:
                return False

            heapq.heappush(heap, -replacedNum)
            total = total - largest + replacedNum


if __name__ == "__main__" :
    solution = Solution()
    print(solution.isPossible([9,3,5]))


            
        