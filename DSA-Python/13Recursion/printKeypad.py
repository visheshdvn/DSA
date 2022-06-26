# Given an integer n, using phone keypad find out and print all the possible strings that can be made using digits of input n.
# Note : The order of strings are not important. Just print different strings in new lines.
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

def keypad(n, string):
    if n//10 == 0:
        end_val = keys.get(n)
        for i in end_val:
            print(string+i)
        return
            
    
    n = str(n)
    a = int(n[0])
    n = int(n[1:])
    val = keys.get(a)
    
    for i in val:
        keypad(n, string+i)
    

n = int(input())
keypad(n, '')