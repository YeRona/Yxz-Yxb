'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        res = ""
        if n == 0:
            return res
        elif n == 1:
            return strs[0]
        ma = len(strs[0])
        for i in range(1, n):
            ma = min(ma, len(strs[i]))
        if ma == 0:
            return res
        m = 0
        flag = 0
        while m < ma:
            ms = strs[0][m]
            for i in range(1, n):
                if strs[i][m] != ms:
                    flag = 1
                    break
            if flag:
                break
            res += ms
            m += 1
        return res