# given an array and a number n,
# left rotate an array by n numbers
# e.g) Input: arr = [1,2,3,4,5] ,  n = 2
# Output = [3,4,5,1,2]

def rotate(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l+=1
        r-=1

def left_rotate(arr, n):
    rotate(arr, 0, n-1)
    rotate(arr, n, len(arr)-1)
    rotate(arr, 0, len(arr)-1)

arr = [int(i) for i in input().strip().split()]
n = int(input())
left_rotate(arr, n)
print("Rotated array: ", arr)