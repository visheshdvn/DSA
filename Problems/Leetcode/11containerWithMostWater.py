from typing import Hashable


class Solution:
    def maxArea(self, height):
        i = 1
        r = len(height)-1
        l = 0
        maxvol = abs(r-l)*min(height[r], height[l])

        while l < r:
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                a1 = abs(l-i)*min(height[l], height[i])
                a2 = abs(i-r)*min(height[i], height[r])

                if a1 <= a2:
                    l += 1
                else:
                    r -= 1

            maxvol = max(maxvol, abs(l-r)*min(height[l], height[r]))
            i += 1
        return maxvol


arr = [int(i) for i in input().strip().split()]
ob = Solution()
print(ob.maxArea(arr))
