def pairStar(str):
    if len(str) == 0:
        return ''

    a = str[0]
    print(a)
    val = pairStar(str[1:])
    
    if val == '' or a != val[0]:
        return a + val
    else:
        return a + '*' + val
    
str = input()
print(pairStar(str))

