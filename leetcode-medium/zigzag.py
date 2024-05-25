# question : https://leetcode.com/problems/zigzag-conversion/


"""

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""


def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    i, direction = 0, 1

    for char in s:
        rows[i] += char
        i += direction
        if i == 0 or i == numRows - 1:
            direction *= -1

    return ''.join(rows)


# Example usage:
s1 = "PAYPALISHIRING"
numRows1 = 3
print(convert(s1, numRows1))  # Output: "PAHNAPLSIIGYIR"

s2 = "PAYPALISHIRING"
numRows2 = 4
print(convert(s2, numRows2))  # Output: "PINALSIGYAHRPI"

s3 = "A"
numRows3 = 1
print(convert(s3, numRows3))  # Output: "A"



