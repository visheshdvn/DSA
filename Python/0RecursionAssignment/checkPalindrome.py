# Check whether a given String S is a palindrome using recursion. Return true or false.
def palindromeCheck(str, n):
    # ans = True
    if n == len(str)//2:
        return True
    
    res = (str[n] == str[-(n+1)])
    
    return res and palindromeCheck(str, n+1)

str = input()
if palindromeCheck(str, 0):
    print('true')
else:
    print('false')