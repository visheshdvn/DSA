# Given a string (lets say of length n), return all the subsequences of the given string.
# Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain same as in the input string.
# Note : The order of subsequences are not important.
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

def subsequences(str):
    if str == '':
        return [str]
    
    char = str[0]
    lst = subsequences(str[1:])
    lst2 = lst[:]
    
    for i in range(len(lst2)):
        lst2[i] = char+lst2[i]
    
    return lst+lst2


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)