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