def stringToInteger(str):
    if len(str) == 0:
        return 0
    
    a = int(str[-1])
    val = stringToInteger(str[:-1])
    return 10*val + a

str = input()
print(stringToInteger(str))