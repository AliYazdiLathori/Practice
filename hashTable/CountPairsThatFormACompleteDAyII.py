"""
Idea:
    A pair of songs forms a complete day pair if the sum of their durations
    is divisible by 24. Instead of checking every pair, group durations by
    their remainder when divided by 24.

Approach:
    - Store indices of hours with the same remainder (hours[i] % 24).
    - For remainders 0 and 12, count pairs inside the same group because they
      can only pair with themselves.
    - For other remainders, multiply the count of remainder `r` by the count
      of remainder `24-r`.
    - Remove the complementary remainder after processing to avoid double
      counting.

Topics:
    - Hash Map
    - Counting
    - Modular Arithmetic

Difficulty:
    Medium

Complexity:
    Time Complexity: O(n)
        # One pass to build the frequency groups and one pass over remainders.

    Space Complexity: O(n)
        # Stores indices grouped by their remainders.
"""


from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hours_section = {}

        for i in range(len(hours)):
            remainder = hours[i] % 24

            if remainder not in hours_section:
                hours_section[remainder] = []

            hours_section[remainder].append(i)
        
        result = 0 

        hours_list = list(hours_section.keys())
        for hour in hours_list:
            length = len(hours_section[hour])
            if hour == 12 or hour == 0:
                result += length * (length-1) /2

            else:

                if (24-hour) not in hours_section:
                    continue
                
                result += length * (len(hours_section[24-hour]))
                hours_list.remove(24-hour)
        
        return int(result)



if __name__ == "__main__":
    s = Solution()
    print(s.countCompleteDayPairs([20,28,12,12,26,12]))  # Output: 4
    print(s.countCompleteDayPairs([1, 2, 3, 4, 5]))  # Output: 0
    print(s.countCompleteDayPairs([12, 12, 12]))     # Output: 3
    print(s.countCompleteDayPairs([0, 24, 48]))      # Output: 3