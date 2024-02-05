def replace_helper(s, a, b, i):
    if len(s) <= i:
        return ""

    char = s[i]
    
    small_s = replace_helper(s, a, b, i+1)
    
    return b + small_s if char == a else char + small_s
    
def replace(s, a, b):
    return replace_helper(s, a, b, 0)

s = input("Enter string: ")
a = input("Enter char a: ")
b = input("Enter char b: ")
print(replace(s, a ,b))