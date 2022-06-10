def maxLengthBetweenEqualCharacters(s):
    d = {}
    max_distance = -1

    for i in range(len(s)):
        found = d.get(s[i], -1)
        if found == -1:
            d[s[i]] = i
        else:
            distance = i-1-found
            if distance > max_distance:
                max_distance = distance

    return max_distance


s = input()
print(maxLengthBetweenEqualCharacters(s))
