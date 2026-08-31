class Solution:
    """
    LeetCode 1137: N-th Tribonacci Number

    Problem: The Tribonacci sequence is defined by T(0)=0, T(1)=1, T(2)=1,
    and T(n) = T(n-1) + T(n-2) + T(n-3) for n >= 3. Given n, return T(n).

    Approach: Iterative bottom-up computation using constant space. Instead
    of storing the whole sequence in an array, only the last three values
    (n_1, n_2, n_3) are kept and rolled forward one step at a time — this
    avoids the O(n) space a full DP array or naive recursion would use.

    Time complexity: O(n) - single loop from 3 to n.
    Space complexity: O(1) - only a fixed number of variables are tracked.
    """

    def tribonacci(self, n: int) -> int:
        # Base cases straight from the problem definition.
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        # n_1, n_2, n_3 track T(i-1), T(i-2), T(i-3) as the loop advances.
        # Initialized to T(2), T(1), T(0) respectively, ready for i=3.
        n_1 = 1
        n_2 = 1
        n_3 = 0

        n_new = 0
        for i in range(3, n+1):
            # T(i) = T(i-1) + T(i-2) + T(i-3)
            n_new = n_3 + n_2 + n_1
            # Slide the window forward: everything shifts down by one.
            n_3 = n_2
            n_2 = n_1
            n_1 = n_new

        return n_new


if __name__ == "__main__":

    solution = Solution()
    print(solution.tribonacci(25))