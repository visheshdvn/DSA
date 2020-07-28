# def uniqueChars(string):
#     if len(string) == 1:
#         return string
    
#     char = string[-1]
#     str = uniqueChars(string[:-1])
    
#     if str.find(char) == -1:
#         return str + char
    
#     return str
    
def uniqueChars(string):
    nstr = ''
    for i in string:
        if i not in nstr:
            nstr += i

    return nstr

# Main
string = input()
print(uniqueChars(string))
