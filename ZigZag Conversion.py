'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        leng = len(s)
        if leng < 3:
            return s
        elif numRows < 2:
            return s
        elif leng <= numRows:
            return s
        t = ""
        cycle = 2 * numRows - 2
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                t += s[i::cycle]
            else:
                for j in range(i, leng, cycle):
                    t += s[j]
                    if j + cycle - 2 * i < leng:
                        t += s[j + cycle- 2 * i]
        return t
