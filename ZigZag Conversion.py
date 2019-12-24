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
        elif numRows == 1:
            return s
        elif leng <= numRows:
            return s
        t = ""
        for i in range(numRows):
            m = i
            if i == 0 or i == numRows - 1:
                while m < leng:
                    t += s[m]
                    m += 2 * numRows - 2
            else:
                flag = 0      # first letter of the group
                while m < leng:
                    if flag == 0:
                        t += s[m]
                        m += 2 * numRows- 2 - 2 * i
                        flag = 1
                    else:
                        t += s[m]
                        m += 2 * i
                        flag = 0
        return t