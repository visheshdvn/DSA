def stockSpan(price,n):
    counter = 1

    for i in range(n):
        j = i-1
        counter = 1
        
        while j>= 0 and price[j] < price[i]:
            counter +=1
            j -= 1

        print(counter, end=' ')
    

n = int(input())
price = [int(ele) for ele in input().split()]
stockSpan(price,n)
# for ele in spans:
#     print(ele,end= ' ')