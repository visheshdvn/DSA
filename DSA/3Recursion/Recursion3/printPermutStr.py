# Print Permutations of a String
# Send Feedback
# Given a string, find and print all the possible permutations of the input string.
# Note : The order of permutations are not important. Just print them in different lines.
# Sample Input :
# abc
# Sample Output :
# abc
# acb
# bac
# bca
# cab
# cba

def printPermutations(string, val):
    if string == '':
        print(val)
        return
    
    n = len(string)
    for i in range(n):
        char = string[i]
        string = string[:i] + string[i+1:]
        printPermutations(string, val+char)
        
        string = string[:i] + char+ string[i:]
        
    

string = input()
printPermutations(string, '')
