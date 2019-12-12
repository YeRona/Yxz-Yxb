class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        t = ""
        s_len = len(s)
        s_rev = []
        if s_len % 2:
            mid = (s_len - 1) // 2
            s_list = list(s)
            s_rev = s_list[s_len - 1:mid:-1]
            if s_rev[: mid] == s_list[: mid]:
                return s
        else:
            mid = (s_len - 2) // 2
            s_list = list(s)
            s_rev = s_list[s_len - 1: mid :-1]    #make fun of the property of list
            if s_rev[: mid + 1] == s_list[:mid + 1]:
                return s
        for i in range(1, s_len + 1):
            t_len = s_len - i
            t += s[t_len]
            #print(i, t_len)
            if t_len % 2:
                mid = (t_len - 1) // 2
                s_list = list(s)
                s_rev = s_list[t_len - 1:mid:-1]
                if s_rev[: mid] == s_list[:mid]:
                    t += s
                    return t
            else:
                mid = (t_len - 2) // 2
                #print(mid, t_len)
                s_list = list(s)
                s_rev = s_list[t_len - 1:mid:-1]
                #print(s_list)
                #print(s_rev)
                if mid == 0:           #consider the special case
                    if s_list[0] == s_list[1]:
                        t += s
                        return t
                    else:
                        t += s[1]
                        t += s
                        return t
                if s_rev[: mid + 1] == s_list[:mid + 1]:
                    t += s 
                    return t
