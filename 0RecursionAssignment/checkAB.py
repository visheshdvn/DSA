# Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise return false.
    
def checkab(str, chars, ind):
    if len(str) <= ind:
        return True
    
    if str[ind] in chars:
        return True and checkab(str, ['a', 'bb'], ind+1)
    
    elif str[ind: ind+2] in chars:
        return True and checkab(str, ['a'], ind+2)
    
    return False

str = input()
if checkab(str, ['a'], 0):
    print('true')
else:
    print('false')
