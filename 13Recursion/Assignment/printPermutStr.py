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
