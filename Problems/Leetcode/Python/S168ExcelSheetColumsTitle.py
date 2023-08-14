from curses import noecho


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        Q = columnNumber // 26
        R = columnNumber % 26

        val = chr(65 + (25 + R) % 26)

        if R == 0:
            Q -= 1

        while Q:
            R = Q % 26
            Q = Q // 26

            c = chr(65 + (25 + R) % 26)
            val = c + val

            if R == 0:
                Q -= 1

        return val

    def titleToNumber(self, columnTitle: str) -> int:
        q = 0

        for i in columnTitle:
            q = 26*q + ord(i)-64

        return q


# n = int(input())
n = input()
ob = Solution()
# print(ob.convertToTitle(n))
print(ob.titleToNumber(n))
