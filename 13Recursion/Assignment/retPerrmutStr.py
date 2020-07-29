def printPermutations(string):
    if len(string) == 1:
        return [string]
    
    n = len(string)
    
    ret_lst = []
    for i in range(n):
        char = string[i]
        string = string[:i] + string[i+1:]
        lst = printPermutations(string)
        
        for j in range(len(lst)):
            a = lst[j]
            a = char+a
            ret_lst.append(a)
            
        string = string[:i] + char+ string[i:]
        
    return ret_lst

string = input()
ans = printPermutations(string)
for i in ans:
    print(i)