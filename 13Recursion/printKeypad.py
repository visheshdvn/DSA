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