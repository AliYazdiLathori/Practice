"""
Idea:
Find the longest subarray where the number of distinct even values is equal
to the number of distinct odd values.

Approach:
- Iterate over every possible starting index.
- Use a set to track distinct numbers in the current subarray.
- Maintain counters for distinct even and odd numbers.
- Update the longest valid length whenever the two counters become equal.
- Ignore duplicate values because they do not affect the count of distinct
  numbers.

Topics:
Hash Set, Sliding Window (Brute Force Expansion), Enumeration

Time Complexity:
O(n^2)
  # For each starting index, the subarray is expanded up to n elements.

Space Complexity:
O(n)
  # The set stores distinct elements of the current subarray.
"""









from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxBal = 0
        for i in range(len(nums)):
            safeIndex = i
            oddNum = 0
            evenNum = 0
            seen = set()
            for j in range(i,len(nums)):
                if nums[j] in seen:
                    if evenNum == oddNum:
                        safeIndex = j  
                    continue

                seen.add(nums[j])
                if nums[j] % 2 == 0:
                    evenNum += 1
                    

                else:
                    oddNum += 1
                    
                
                if evenNum == oddNum:
                    safeIndex = j
            if i != safeIndex:
                maxBal = max (maxBal, safeIndex-i+1)
        return maxBal

                    


        
if __name__ == "__main__":
    s = Solution()
    print(s.longestBalanced([1,2,3,4,5,6]))  # Output: 6
    print(s.longestBalanced([1,2,3,4,5]))    # Output: 4
    print(s.longestBalanced([1,1,1,1]))      # Output: 0
    print(s.longestBalanced([2,4,6,8]))      # Output: 0
    print(s.longestBalanced([1,3,5,7]))      # Output: 0
    print(s.longestBalanced([1,2,3,4,5,6,7]))# Output: 6