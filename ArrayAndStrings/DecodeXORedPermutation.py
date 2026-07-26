"""
Idea:
    Recover the first element of the permutation by analyzing the bitwise
    relationship between consecutive XOR values. For each bit position, track
    whether each element has the same or opposite bit as the first element.
    Then reconstruct the first number using the known sum of the permutation,
    and rebuild the entire permutation using XOR.

Approach:
    - Compute, for every bit, how many permutation elements share the same bit
      as the first element.
    - Use the total sum of numbers from 1 to n and binary addition (with carry)
      to determine each bit of the first element.
    - Once the first value is known, reconstruct the permutation by repeatedly
      applying:
          perm[i + 1] = perm[i] ^ encoded[i]

Topics:
    - Bit Manipulation
    - XOR
    - Binary Arithmetic
    - Simulation

Difficulty:
    Hard

Complexity:
    Time Complexity: O(n * log n)
        # Each encoded value is processed across all bit positions.

    Space Complexity: O(log n)
        # Stores bit relations and counts; output array excluded.
"""

class Solution:

    def update_relation(self, value, relation, bits):
        """
        relation[i] = 1  -> current number has the same bit as first number
        relation[i] = -1 -> current number has the opposite bit from first number
        """

        binary = format(value, f"0{bits}b")

        for i, bit in enumerate(binary):
            if bit == "1":
                relation[i] *= -1

        return relation

    def decode(self, encoded):
        n = len(encoded) + 1

        # Values from 1 to n require this many bits
        bits = n.bit_length()

        relation = [1] * bits
        same_count = [1] * bits

        for value in encoded:
            relation = self.update_relation(
                value,
                relation,
                bits
            )

            for i in range(bits):
                if relation[i] == 1:
                    same_count[i] += 1

        total_sum = n * (n + 1) // 2

        first_bits = [0] * bits
        carry = 0

        # i is an index from MSB to LSB in first_bits.
        # The loop processes columns from LSB to MSB.
        for i in range(bits - 1, -1, -1):
            bit_position = bits - 1 - i

            # Extract the corresponding bit from total_sum
            sum_bit = (total_sum >> bit_position) & 1

            ones_if_first_is_one = same_count[i]
            ones_if_first_is_zero = n - same_count[i]

            if (ones_if_first_is_one + carry) % 2 == sum_bit:
                first_bits[i] = 1
                ones = ones_if_first_is_one
            else:
                first_bits[i] = 0
                ones = ones_if_first_is_zero

            carry = (ones + carry) // 2

        first = int("".join(map(str, first_bits)), 2)

        perm = [first]

        for value in encoded:
            perm.append(perm[-1] ^ value)

        return perm

if __name__ == '__main__':
    solution = Solution()
    encoded = [6,5,4,6]
    result = solution.decode(encoded)
    print(result)  # Output: [2, 4, 1, 5, 3]