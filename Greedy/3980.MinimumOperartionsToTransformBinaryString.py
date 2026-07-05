"""
Idea:
Greedily transform `s1` into `s2` by first fixing all `0 -> 1` mismatches,
then resolving remaining `1 -> 0` mismatches using the cheapest available
operation based on the next character.

Approach:
- Convert both strings to lists for in-place updates.
- First pass: flip every required `0 -> 1` mismatch.
- Second pass: handle `1 -> 0` mismatches greedily by checking the adjacent
  character and choosing the minimum-cost operation.
- If the final mismatch cannot be resolved, return `-1`.

Topics:
Greedy, String, Simulation

Time Complexity:
O(n)

Space Complexity:
O(n)  # Due to converting strings into mutable lists.
"""

class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        s1 = list(s1)
        s2 = list(s2)
        moves = 0
        for i in range(len(s1)):
            if s1[i] == '0' and s2[i] == '1':
                s1[i] = '1'
                moves += 1
        
        
        for i in range(len(s1)):
            if s1[i] == '1' and s2[i] == '0' and i < len(s1)-1:
                if s1[i+1] == '1' and s2[i+1] == '0':
                    moves += 1
                    s1[i] = '0'
                    s1[i+1] = '0'

                elif s1[i+1] == '0' and s2[i+1] == '0':
                    moves += 2
                    s1[i] = '0'
                
                elif s1[i+1] == '1' and s2[i+1] == '1':
                    moves += 2
                    s1[i] = '0'
            elif i == len(s1)-1:
                if s1 == s2:
                    return moves

                elif s1[i-1] == s2[i-1] :
                    moves += 2
                    s1[i] = s2[i]
                else:
                    return -1
                    
        
        return moves

if __name__ == "__main__":
    s1 = "1100"
    s2 = "0011"
    print(Solution().minOperations(s1, s2))  # Output: 4