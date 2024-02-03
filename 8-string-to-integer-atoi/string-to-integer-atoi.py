class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # i = 0
        # while i < len(s) and s[i] == ' ':
        #     i += 1
        # s = s[i:]  # i ---> last of string
        s=s.strip()
        sign = 1
        ans = 0
        if s and s[0] == '-':
            sign = -1
        MAX = 2**31 - 1
        MIN = -2**31
        i = 1 if s and (s[0] == '+' or s[0] == '-') else 0
        while i < len(s):
            if s[i] == ' ' or not s[i].isdigit():
                break
            ans = ans * 10 + int(s[i])
            if sign == -1 and -1 * ans < MIN:
                return MIN
            if sign == 1 and ans > MAX:
                return MAX
            i += 1
        return sign * ans