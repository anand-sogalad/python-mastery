"""
476. Number Complement
Easy
Topics
premium lock icon
Companies
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.



Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


Constraints:

1 <= num < 231
"""


class Solution:
    def find_complement(self, num):
        mask = (1 << num.bit_length()) - 1
        return mask ^ num


print(Solution().find_complement(5))


"""
Task
Given an integer,n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

"""


def is_even(n):
    return n % 2 == 0


def logical_condition(n: int):
    if not is_even(n):
        return "Weird"
    if n in range(2, 6):
        return "Not Weird"
    if n in range(6, 21):
        return "Weird"
    if n > 20:
        return "Not Weird"
