def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False

    i, j = 0, 0

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    if i == len(s):
        return True

    return False


s = input()
t = input()
print(isSubsequence(s, t))
