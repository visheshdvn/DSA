# Question) You are given with an array of integers and an integer K. Write a program to find and print all pairs which have difference K.
# Take difference as absolute.

from collections import Counter

def printPairDiffK(n, a, diff):
    counter_dict = Counter(a)
    a = sorted(a, reverse=True)
    # print(a)
    
    i = 0
    while i < n:
        counter_dict[a[i]] -= 1
        count = counter_dict.get(a[i] - diff, 0)
        
        while count:
            print(a[i]-diff, a[i])
            count -= 1
        
        i += 1
        

n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(n, l, k)