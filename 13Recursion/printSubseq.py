# Given a string (lets say of length n), print all the subsequences of the given string.
# Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain same as in the input string.
# Note : The order of subsequences are not important. Print every subsequence in new line.
# Sample Input:
# abc
# Sample Output:
# "" (the double quotes just signifies an empty string, don't worry about the quotes)
# c 
# b 
# bc 
# a 
# ac 
# ab 
# abc 

def printSubs(s, o):
    if len(s) == 0:
        print(o)
        return
    
    printSubs(s[1:], o)
    
    newOutput = o+s[0]
    printSubs(s[1:], newOutput)

s = input()
printSubs(s, '')