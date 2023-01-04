
def merge(nums1, m, nums2, n):
    i = -1
    j = -1
    k = 0
    if m-1 >= 0:
        k = m-1

    while j >= -len(nums2):
        if nums2[j] > nums1[k]:
            nums1[i] = nums2[j]
            i -= 1
            j -= 1
        elif nums1[k] > nums2[j]:
            nums1[i] = nums1[k]
            nums1[k] = 0
            i -= 1
            if k-1 >= 0:
                k -= 1
        else:
            nums1[i] = nums2[j]
            j -= 1
            i -= 1


nums1 = [int(i) for i in input().split()]
m = int(input())
nums2 = [int(i) for i in input().split()]
n = int(input())
merge(nums1, m, nums2, n)
print(*nums1)
