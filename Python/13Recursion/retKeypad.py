# Given an integer n, using phone keypad find out all the possible strings that can be made using digits of input n.
# Note : The order of strings are not important.
# Input Format :
# Integer n
# Output Format :
# All possible strings in different lines
# Constraints :
# 1 <= n <= 10^6
# Sample Input:
# 23
# Sample Output:
# ad
# ae
# af
# bd
# be
# bf
# cd
# ce
# cf

keys = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

def keypad(n):
    if n//10 == 0:
        return list(keys.get(n))
    
    num = n%10
    lst = keypad(n//10)
    chars = list(keys.get(num))
    
    to_ret = []
    
    for i in lst:
        for j in chars:
            small_str = i+j
            to_ret.append(small_str)
    
    return to_ret

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)
    