def equilibriumIndex(n, arr):
    sum_right = sum(arr) - arr[0]
    sum_left = 0
    # print('init sums', sum_left, sum_right)
    i = 0
    
    while i < n:
        # print('sums', sum_left, i, sum_right)
        if i == n-1 and sum_left != 0:
            return -1
        
        if sum_left == sum_right:
            # print('returning')
            return i
        
        sum_right -= arr[i+1]
        sum_left += arr[i]
        
        i += 1

# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(n, arr))
