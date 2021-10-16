from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        max_len = 0

        while right < len(s):
            if s[right] in s[left: right]:
                while s[right] in s[left: right] and left < right:
                    left += 1

            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len


s = input()
ob = Solution()
print(ob.lengthOfLongestSubstring(s))
