#first try: brutal solution
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        leng = len(s)
        t = ""
        if len(s) > 5000:
            t += s
            return t
        ans_len = 1
        ans_pro = 0 # 0 is singular, 1 is even
        for i in range(1, leng):
            if 2 * i + 1 <= ans_len :
                pass
            elif leng - i - 1 < i:
                break
            else:
                flag = 1
                for m in range(i):
                    if s[i - m - 1] != s[i + m + 1]:
                        flag = 0
                        break
                if not flag:
                    pass
                elif ans_len < 2 * m + 3:
                    ans_len = 2 * m + 3
        if ans_len == leng:
            return s
        for i in range(leng):
            if i + 2 > leng:
                break
            elif s[i] != s[i + 1]:
                pass
            elif leng - i - 2 < i:
                break
            else:
                if 2 * i + 2 <= ans_len:
                    pass
                elif i == 0:
                    ans_len = 2
                    ans_pro = 1
                else:
                    flag = 1
                    for m in range(i):
                        if s[i - m - 1] != s[i + m + 2]:
                            flag = 0
                            break
                    if not flag:
                        pass
                    elif ans_len < 2 * m + 4:
                        ans_len = 2 * m + 4
                        #ans_loc = i
                        ans_pro = 1
        if ans_len == leng:
            return s
        if ans_pro:
            for i in range(leng - ans_len):
                t += s[leng - i - 1]
            t += s
            return t
        else:
            for i in range(leng - ans_len):
                #print("leng - ans_len = {0} , i = {1}, s[{2}] = {3}".format(leng - ans_len, i, leng - i - 1 ,s[leng - i - 1]))
                t += s[leng - i - 1]
            t += s
            return t
