from collections import Counter
def maxFreq(l):
    counter_dict = Counter(l)
    
    element = (l[0], counter_dict[l[0]])
    
    for i in l:
        if counter_dict[i] > element[1]:
            element = (i, counter_dict[i])
            
    return element[0]
            

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))
