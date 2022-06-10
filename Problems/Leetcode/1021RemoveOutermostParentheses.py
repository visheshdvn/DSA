from re import sub


def removeOuterParentheses(s):
    subs = ""
    l = 0

    for i in s:
        if i == "(":
            l += 1
            if l > 1:
                subs += i

        if i == ")":
            l -= 1
            if l > 0:
                subs += i

    return subs


s = input()
print(removeOuterParentheses(s))
