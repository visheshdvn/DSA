# Given a random integer array A of size N. Find and print the pair of elements in the array which sum to 0.
# Array A can contain duplicate elements.
# While printing a pair, print the smaller element first.
# That is, if a valid pair is (6, -6) print "-6 6". There is no constraint that out of 5 pairs which have to be printed in 1st line. You can print pairs in any order, just be careful about the order of elements in a pair.

# Input format :
# Line 1 : Integer N (Array size)
# Line 2 : Array elements (separated by space)
# Output format :
# Line 1 : Pair 1 elements (separated by space)
# Line 2 : Pair 2 elements (separated by space)
# Line 3 : and so on

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