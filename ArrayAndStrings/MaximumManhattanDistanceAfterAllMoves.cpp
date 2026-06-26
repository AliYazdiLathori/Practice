/*
    Problem: Maximum Manhattan Distance After All Moves
    Platform: LeetCode
    Difficulty: Medium

    Topic:
    - Manhattan Distance
    - String Manipulation

    Time Complexity: O(n)
    Space Complexity: O(1)

    Author: Ali
    Date: 2026-06-27
*/

#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int maxDistance(string moves) {
        int maxDistanceHorizantal = 0;
        int maxDistanceVertical = 0;
        int extraDistance = 0;
        int maxManhattanDistance = 0;
        for (int i = 0; i < moves.length(); i++) {
            if (moves[i] == 'L') {
                maxDistanceHorizantal++;
            } else if (moves[i] == 'R') {
                maxDistanceHorizantal--;
            } else if (moves[i] == 'U') {
                maxDistanceVertical++;
            } else if (moves[i] == 'D') {
                maxDistanceVertical--;
            } else {
                extraDistance++;
            }
        }
        maxManhattanDistance = abs(maxDistanceHorizantal) +
                               abs(maxDistanceVertical) + abs(extraDistance);
        return maxManhattanDistance;
    }
};

int main() {
    Solution sol;
    cout << sol.maxDistance("L_D_") << endl;  // Test case
    return 0;
}