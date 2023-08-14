from typing import List

class Solution(object):
    def moveDigits(self, arr, i, j):
        for k in range(j, i, -1):
            arr[k] = arr[k-1]

        
    def duplicateZeros(self, arr: List[int]) -> None:
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                self.moveDigits(arr, i, len(arr)-1)
                i+=1
            i+=1
        
    
arr = [int(i) for i in input().split()]
ob = Solution()
ob.duplicateZeros(arr)
print(arr)
