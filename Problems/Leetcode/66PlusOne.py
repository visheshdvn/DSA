from unicodedata import digit


class Solution:
    def plusOne(self, digits):
        carry = 1
        new_digits = []

        for i in range(-1, -len(digits)-1, -1):
            n = digits[i] + carry
            carry = n // 10
            num = n % 10
            new_digits.append(num)

        if carry == 1:
            new_digits.append(1)
            
        return reversed(new_digits)


digits = [int(i) for i in input().split()]
ob = Solution()
sol = ob.plusOne(digits)
print(*sol)
