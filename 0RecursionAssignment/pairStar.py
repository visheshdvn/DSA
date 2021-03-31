# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
def pairStar(str):
    if len(str) == 0:
        return ''

    a = str[0]
    # print(a)
    val = pairStar(str[1:])
    
    if val == '' or a != val[0]:
        return a + val
    else:
        return a + '*' + val
    
str = input()
print(pairStar(str))