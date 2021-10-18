class Solution:
    def longestPalindrome(self, s):
        # In this function l and r are the middle indecees, as palindrome is created from the middle, we expand from inner (middle) to outer
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # l+1 because we take the previous sliceas when we exit the while loop it will no longer be palindromic
            return s[l+1:r]

        res = ""
        for i in range(len(s)):
            odd = helper(i, i)  # odd case, like "aba"
            even = helper(i, i+1)  # even case, like "abba"
            # compare between odd,even and res according to the max length
            res = max(odd, res, even, key=lambda x: len(x))

        return res


s = input()
ob = Solution()
print(ob.longestPalindrome(s))
