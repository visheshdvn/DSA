def addStr(num1, num2):
    n1 = len(num1)
    n2 = len(num2)

    num1 = num1[::-1]
    num2 = num2[::-1]

    i, j = 0, 0
    carry = 0
    ans = ""

    while i < n1 and j < n2:
        s = int(num1[i]) + int(num2[j]) + carry
        ans += str(s % 10)
        carry = s // 10
        i += 1
        j += 1

    while i < n1:
        s = int(num1[i]) + carry
        ans += str(s % 10)
        carry = s//10
        i += 1

    while j < n2:
        s = int(num2[j]) + carry
        ans += str(s % 10)
        carry = s//10
        j += 1

    if carry > 0:
        ans += str(carry)

    return ans[::-1]


num1 = input()
num2 = input()

print(addStr(num1, num2))
