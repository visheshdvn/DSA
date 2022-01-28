# Problem: Remove 'x' from string
def removeX(s): 
    if len(s) == 0:
        return s
    
    smallOutput = removeX(s[1:])
    
    if s[0] == 'x':
        return smallOutput
    else:
        return s[0] + smallOutput

# Main
string = input()
print(removeX(string))
