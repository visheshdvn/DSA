def maxDepth(s):
    maxDepth = 0
    currDepth = 0
    # stack = []

    for i in s:
        if i == "(":
            # stack.append(i)
            currDepth += 1

        if i == ")":
            if currDepth > maxDepth:
                maxDepth = currDepth

            # stack.pop()
            currDepth -= 1

    return maxDepth


s = input()
print(maxDepth(s))
