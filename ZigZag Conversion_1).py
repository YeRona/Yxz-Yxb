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
    def convert(self, s, numRows):
        """
        s: "ABCDEFGHIJKL"
        numRows: 3
        outp: ["AEI","BDFHJL","CGK"]
        outputStr: "AEIBDFHJL"
        """
        lin = 0
        pl = 1
        outp = [""] * numRows
        for i in range(len(s)):
            outp[lin] += s[i]
            if numRows > 1:
                lin += pl
                if lin == 0 or lin == numRows -1:
                    pl *= -1
        outputStr = ""
        for j in range(numRows):
            outputStr += outp[j]
        return outputStr
