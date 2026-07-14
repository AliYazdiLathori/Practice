"""
Idea:
Use a fixed-size sliding window to maintain the sum of each subarray of length
`k`. Instead of recomputing the sum each time, update it in O(1) by removing
the outgoing element and adding the incoming one.

Approach:
- Initialize the first window of size `k` and compute its sum.
- Slide the window one position at a time:
  - Check if the current window sum is at least `k * threshold`.
  - Remove the leftmost element and add the next element.
- Count all windows satisfying the condition.

Topics:
Sliding Window, Queue (Deque), Array

Time Complexity:
O(n)
  # Each element enters and leaves the window exactly once.

Space Complexity:
O(k)
  # The deque stores at most k elements.
"""

from collections import deque
from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        queue = deque()
        #initilizing first substring
        for i in range(k):
            queue.append(arr[i])
        
        counter = 0
        sumSubArray = sum(queue)
        for i in range(k-1, len(arr)):

            if sumSubArray >= k * threshold:
                counter += 1
            
            if i >= len(arr)-1:
                return counter
            
            sumSubArray = sumSubArray - (queue.popleft()) + arr[i+1]
            queue.append(arr[i+1]) 
        
if __name__ == "__main__":
    arr = [2, 1, 3, 4, 1]
    k = 3
    threshold = 2
    solution = Solution()
    result = solution.numOfSubarrays(arr, k, threshold)
    print(result)  # Output: 3