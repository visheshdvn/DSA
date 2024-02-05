def replacePi(s):
    if s == "":
        return ""
    
    # return '3.14' + replacePi(s[2:]) if s[0:2] == 'pi' else s[0] + replacePi(s[1:])
    
    if s[0:2] == 'pi':
        return '3.14' + replacePi(s[2:])
    else:
        return s[0] + replacePi(s[1:])

s = input("Enter string: ")
print(replacePi(s))