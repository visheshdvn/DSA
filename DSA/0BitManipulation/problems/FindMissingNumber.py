# from array import array


# Given an array of n numbers that has values in the range [1, n+1] and each num appearing exactly once.
# Find the missing number;


# solution
arr = [1, 2, 3, 5]
n = 0

for i in arr:
    n ^= i

for i in range(1, len(arr)+2):
    n ^= i

print(n)
