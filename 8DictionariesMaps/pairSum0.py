from collections import Counter

def pairSum0(l):
    counterD = Counter(l)
    
    for i in l:
        x = y = 0
        try:
            x = counterD.pop(i)
            y = counterD.pop(-i)
            
            for j in range(x*y):
                if -i < i:
                    print(-i, i)
                else:
                    print(i, -i)
                    
        except:
            continue
    
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
pairSum0(l)