"""""Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Constraints:
-231 <= x <= 231 - 1"""


def reverse_integer(x):
    # Define the range limits
    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1

    # Handle negative numbers
    sign = 1 if x >= 0 else -1
    x = abs(x)

    # Reverse the digits of x
    reversed_x = 0
    while x != 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10

    # Check if the reversed integer is within the 32-bit range
    reversed_x *= sign
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0
    else:
        return reversed_x


# Test cases
print(reverse_integer(123))  # Output: 321
print(reverse_integer(-123))  # Output: -321
print(reverse_integer(120))  # Output: 21
