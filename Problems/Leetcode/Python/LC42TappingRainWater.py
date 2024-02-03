class Solution:
    def trap(self, height):
        n = len(height)
        lmax, rmax = [0]*n, [0]*n
        lm = float("-inf")
        rm = float("-inf")
        water = 0

        for i in range(n):
            lmax[i] = lm = max(lm, height[i])

        for j in range(-1, -n-1, -1):
            rmax[j] = rm = max(rm, height[j])

        for i in range(n):
            water += min(lmax[i], rmax[i]) - height[i]

        return water


arr = [int(i) for i in input().strip().split()]
ob = Solution()
print(ob.trap(arr))
