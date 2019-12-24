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
        if n == 0:
            return ""
        elif n == 1:
            return strs[0]
        ma = len(strs[0])
        for i in range(1, n):
            ma = min(ma, len(strs[i]))
        if ma == 0:
            return ""
        leng = min(len(strs[0]),len(strs[1]))
        resu = ""
        for i in range(leng):
            if strs[0][i] == strs[1][i]:
                resu += strs[0][i]
            else:
                break
        res = resu
        for i in range(2,n):
            leng = min(len(res),len(strs[i]))
            resu = ""
            for j in range(leng):
                if res[j] == strs[i][j]:
                    resu += res[j]
                else:
                    break
            res = resu
        return res
