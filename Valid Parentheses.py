'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        h = []
        dic = {"]":"[", "}": "{", ")": "("}
        for i in s:
            if i in ["(", "{", "["]:
                h.append(i)
            else:
                if not h:
                    return False
                t = h.pop()
                if t != dic[i]:
                    return False
        if not h:
            return True
        else:
            return False