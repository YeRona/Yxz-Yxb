'''
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        PP = set()
        if n == 1:
            PP = {"()"}
        else:
            CC = self.generateParenthesis(n - 1)
            for i in CC:
                m = "()" + i
                PP.add(m)
                m = i + "()"
                PP.add(m)
                m = "(" + i + ")"
                PP.add(m)
            for i in range(2, n // 2 + 1):
                AA = self.generateParenthesis(i)
                BB = self.generateParenthesis(n - i)
                for j in AA:
                    for k in BB:
                        m = j + k
                        PP.add(m)
                        m = k + j
                        PP.add(m)
        PP = list(PP)
        return PP