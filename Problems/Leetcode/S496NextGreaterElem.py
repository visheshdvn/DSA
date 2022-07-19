class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        g_indx = {k: ind for ind, k in enumerate(nums1)}
        ret_list = [-1]*len(nums1)

        for i in range(len(nums2)):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                ret_list[g_indx[stack[-1]]] = nums2[i]
                stack.pop()

            if g_indx.get(nums2[i], -1) != -1:
                stack.append(nums2[i])

        return ret_list


nums1 = [int(i) for i in input().split()]
nums2 = [int(i) for i in input().split()]

ob = Solution()
lst = ob.nextGreaterElement(nums1, nums2)
print(lst)
