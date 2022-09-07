from collections import Counter

def SumInArray(n, a, sum):
    num_counts = Counter(a)
    # print(num_counts)

    i = 0
    while i < n:
        num_counts[a[i]] -= 1
        count = num_counts.get(sum - a[i], 0)
        while count:
            if a[i] <= sum - a[i]:
                print(a[i], sum - a[i])
            else:
                print(sum - a[i], a[i])
            count -= 1
        
        i += 1
        

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
sum=int(input())
SumInArray(n, arr, sum)
