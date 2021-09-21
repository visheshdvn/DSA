class Solution:
    def longestCommonPrefix(self, strs):
        cstr = {}
        min_len = 300
        min_str = ""

        for i in strs:
            if len(i) < min_len:
                min_Str = i
                min_len = len(i)
        
        for k, v in enumerate(min_Str):
            cstr[k] = v
        
        # commonLength = min_len
        for i in strs:
            for p, s in enumerate(i[:min_len]):
                if s != cstr[p]: 
                    min_len = p
                    break
        
        return min_Str[:min_len]


strs = input().strip().split()
ob = Solution()
print(ob.longestCommonPrefix(strs))
