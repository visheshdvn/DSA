
def merge(nums1, m: int, nums2, n: int):
    nums1_index = m-1
    nums2_index = n-1
    index = m+n-1
    
    while(nums1_index>=0 and nums2_index>=0):
        if(nums1[nums1_index]<nums2[nums2_index]):
            nums1[index]=nums2[nums2_index]
            nums2_index-=1
        else:
            nums1[index]=nums1[nums1_index]
            nums1_index-=1
        index-=1
    
    while(nums2_index>=0):
        nums1[index]=nums2[nums2_index]
        nums2_index-=1
        index-=1
            
    return nums1


nums1 = [int(i) for i in input().split()]
m = int(input())
nums2 = [int(i) for i in input().split()]
n = int(input())
merge(nums1, m, nums2, n)
print(*nums1)
