# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(s):
    if len(s) == 0 or len(s) == 1:
        return s
    
    count = 1
    for i in range(len(s) -1):
        if s[i] == s[i+1]:
            count +=1
        else:
            break
        
    return s[0] + removeConsecutiveDuplicates(s[count:])

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
