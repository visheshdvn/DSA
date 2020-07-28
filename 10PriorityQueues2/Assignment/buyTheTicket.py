def timeTaken(lst, k):
    
    time_count = 0
    
    while True:
        if k == -1:
            return time_count
        
        coming = lst[0]
        
        if coming != max(lst):
            lst = lst[1:]
            lst.append(coming)
            k -= 1
            
            if k < 0:
                k = len(lst) -1
                
            continue
        
        lst = lst[1:]
        k -= 1
        time_count += 1
        

n = int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=timeTaken(lst, k)
print(ans)