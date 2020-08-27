# Question) You are given an array of unique integers that contain numbers in random order. Write a program to find the longest possible sequence of consecutive numbers using the numbers from given array.
# You need to return the output array which contains consecutive elements. Order of elements in the output is not important.
# Best solution takes O(n) time.
# If two sequences are of equal length then return the sequence starting with the number whose occurrence is earlier in the array.

# Sample Input 1 :
# 13
# 2 12 9 16 10 5 3 20 25 11 1 8 6 
# Sample Output 1 :
# 8 
# 9 
# 10 
# 11 
# 12

def longestConsecutiveSeq(n, arr):
    if n == 1:
        print(arr[0])
        return
    
    sorted_arr = sorted(arr)
    max_ind_start = 10000
    max_count = 0
    
    curr_ind = -1
    count = 0
    
    for i in range(n):
        
        if i < n-1 and sorted_arr[i+1] == sorted_arr[i] + 1:
            if curr_ind == -1:
                curr_ind = i
            count += 1
            continue
            
            
        if sorted_arr[i] == sorted_arr[i-1] + 1:
            count += 1
            if max_count < count:
                max_count = count
                max_ind_start = curr_ind
                count = 0
                curr_ind = -1
                
            if max_count == count and arr.index(sorted_arr[curr_ind]) < arr.index(sorted_arr[max_ind_start]):
                max_count = count
                max_ind_start = curr_ind
                count = 0
                curr_ind = -1
                
            if max_count > count:
                count = 0
                curr_ind = -1
    
    for i in sorted_arr[max_ind_start: max_ind_start+max_count]:
        print(i)
    
    
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
longestConsecutiveSeq(n, l)