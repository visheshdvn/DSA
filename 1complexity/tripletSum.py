from collections import Counter
def ncr(a, b):
    prod_a = prod_b = 1
    while b:
        prod_a *= a
        prod_b *= b
        a-=1
        b-=1
    return prod_a // prod_b

def tripletSum(n, arr, num):
    # print(arr)
    counts = Counter(arr)
    # print(counts)
    set_arr = list(set(arr))
    set_arr.sort()
    # print(set_arr)
    lset = len(set_arr)

    for i in range(lset):
        num1 = set_arr[i]
        sum_to_find = num - num1

        j = i
        while j < lset:
            num2 = set_arr[j]
            
            num3 = sum_to_find - num2
            if num3 < num1 or num3 < num2:
                break

            if num3 > set_arr[-1]:
                j+=1
                continue
            
            # print(num1, num2, num3)
            # print('filtered')
            counts2 = Counter([num1, num2, num3])
            workable = True
            counts2_list = counts2.keys()
            for k in counts2_list:
                if counts2[k] > counts[k]:
                    workable = False
                    break

            if workable:
                # print('workable triplet',num1, num2, num3)
                product = 1
                # print('list detail',counts2, counts2_list)
                for i in counts2_list:
                    product *= ncr(counts[i], counts2[i])
                    # print('counts2', i, counts2, counts2.get(i, 0))
                    # print('counts: ', i, counts, counts.get(i, 0))
                
                while product:
                    print(num1, num2, num3)
                    product -= 1
            j+=1


n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
num=int(input())
tripletSum(n, arr, num)

# ##############
# print('iter solution')
# from itertools import combinations 
  
# def tripletSum(lst, key): 
      
#     def valid(val): 
#         return sum(val) == key 
          
#     return list(filter(valid, list(combinations(lst, 3)))) 
  
# # n=int(input())
# lst = list(int(i) for i in input().strip().split(' '))
# lst.sort()
# num = int(input())
# ll = tripletSum(lst, num)
# for i in ll:
#     a, b, c = i
#     print(a, b, c)