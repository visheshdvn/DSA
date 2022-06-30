# Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.
def stringToInteger(str):
    if len(str) == 0:
        return 0
    
    a = int(str[-1])
    val = stringToInteger(str[:-1])
    return 10*val + a

str = input()
print(stringToInteger(str))