class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 1:
            return 1

        curr = 1
        n = 1

        while n < len(nums):
            if curr == n and nums[curr] != nums[curr-1]:
                nums[curr] = nums[n]
                curr += 1
                n += 1
            elif (curr == n and nums[curr] == nums[curr-1]) or (curr != n and nums[curr] == nums[n]):
                n += 1
            elif curr != n and nums[curr] != nums[n]:
                if not nums[n] == nums[curr-1]:
                    nums[curr] = nums[n]
                    curr += 1
                n += 1

        return curr


x = [int(i) for i in input().strip().split()]
ob = Solution()
n = ob.removeDuplicates(x)
print(n)
# print(list(set(x)))
# print(n == len(list(set(x))))
print(x[:n])
