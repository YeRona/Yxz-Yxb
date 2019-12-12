class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        t = ""
        s_len = len(s)
        if s_len % 2:
            mid = (s_len - 1) // 2
            flag = 1
            for i in range(1, mid + 1):
                if s[mid - i] != s[mid + i]:
                    flag = 0
                    break
            if flag == 1:
                return s
        else:
            mid = (s_len - 2) // 2
            flag = 1
            for i in range(mid + 1):
                if s[mid - i] != s[mid + i + 1]:
                    flag = 0
                    break
            if flag == 1:
                return s
        for i in range(1, s_len + 1):
            t_len = s_len - i
            t += s[t_len]
            if t_len % 2:
                mid = (t_len - 1) // 2
                flag = 1
                for m in range(1, mid + 1):
                    if s[mid - m] != s[mid + m]:
                        flag = 0
                        break
                if flag == 1:
                    #print(t_len, mid, t)
                    t += s
                    return t
            else:
                mid = (t_len - 2) // 2
                flag = 1
                for m in range(mid + 1):
                    if s[mid - m] != s[mid + m + 1]:
                        flag = 0
                        break
                if flag == 1:
                    t += s
                    return t