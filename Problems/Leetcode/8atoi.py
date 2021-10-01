class Solution:
    def myAtoi(self, s):
        if s == "":
            return 0
        s = s.strip()
        multiplier = 1
        if s[0] == "-":
            multiplier = -1
            s = s[1:]
            
        elif s[0] == "+":
            s = s[1:]
            
        num_s = 0
        for i in s:
            if 48 <= ord(i) <= 57:
                num_s = num_s*10 + int(i)
                continue
            break

        s = multiplier * num_s

        # return multiplier * s
        if s < -1*2**31:
            return -1*2**31
        elif s > 2**31-1:
            return 2**31-1
        else:
            return s


n = input()
ob = Solution()
print(ob.myAtoi(n))
