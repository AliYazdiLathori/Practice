"""
Idea:
    Split the points into those that can appear before the pivot and those
    that can appear after it. The answer is the Longest Increasing Subsequence
    (LIS) on each side plus the pivot itself.

Approach:
    - Use the pivot coordinates to partition the points:
        - Backward: x < pivot.x and y < pivot.y
        - Forward:  x > pivot.x and y > pivot.y
    - Sort each set by x ascending and y descending to correctly handle
      duplicate x-values.
    - Apply the patience sorting algorithm with binary search to find the
      LIS based on the y-coordinate.
    - Return:
          LIS(backward) + 1 + LIS(forward)

Topics:
    - Longest Increasing Subsequence (LIS)
    - Patience Sorting
    - Binary Search
    - Sorting
    - Dynamic Programming (Optimization)

Difficulty:
    Hard

Complexity:
    Time Complexity: O(n log n)
        # Partitioning is O(n), sorting and LIS each take O(n log n).

    Space Complexity: O(n)
        # Stores the partitioned point sets and LIS tails.
"""


from typing import List


    

class Solution:
    def binary_search(self, tails, target):
        Left, Right = 0, len(tails)-1
        while Left < Right:
            mid = (Left+Right)//2
            if tails[mid][1] < target[1]:
                Left = mid + 1
            else:
                Right = mid
        tails[Left] = target
            
    def LIS(self, list) -> int:
        if not list:
            return 0

        #patient sorting algorithm
        tails = []
        tails.append(list[0])
        for num in list[1:]:
            if num[1] > tails[-1][1]:
                tails.append(num)
                continue

            self.binary_search(tails, num)

        return len(tails)
                



        
        
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        #Preprocess, remove invalid coordinates and create two distinct set
        #The forward_set is the set of coordinates which its elements' x and y are bigger than coordinate[k](pivot)
        #The Backward_set is the set of coordinates which its elements' x and y are smaller than coordinate[k](pivot)
        pivot = coordinates[k]
        forward_set = []
        backward_set = []
        for coordinate in coordinates:
            if coordinate[0] > pivot[0] and coordinate[1] > pivot[1]:
                forward_set.append(coordinate)
            elif coordinate[0] < pivot[0] and coordinate[1] < pivot[1]:
                backward_set.append(coordinate)

        forward_set.sort(key=lambda p: (p[0], -p[1]))

        max_forward_length = self.LIS(forward_set)

        backward_set.sort(key=lambda p: (p[0], -p[1]))

        max_backward_length = self.LIS(backward_set)

        result = max_forward_length + max_backward_length + 1  # +1 for the pivot itself

        return result

            
        
            
if __name__ == "__main__":
    sol = Solution()
    coordinates = [[8,6],[1,7],[6,3],[1,5],[9,9],[0,0],[0,4],[0,5],[6,9]]
    k = 6
    result = sol.maxPathLength(coordinates, k)
    print(result)  # Output the result



            
     