def reverseStack(s1,s2):
    if s1 == []:
        return

    s2.append(s1.pop())

    reverseStack(s1, s2)
    a = s2.pop(0)
    s1.append(a)

from sys import setrecursionlimit
setrecursionlimit(11000)
n = int(input())
s1 = [int(ele) for ele in input().split()]
s2 = []
reverseStack(s1,s2)
while(len(s1) !=0):
    print(s1.pop(),end= ' ')