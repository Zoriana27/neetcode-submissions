class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        the_substring = ""
        def expand(l, r, s):
            indices = (0, 0)
            W = 0
            while l >= 0 and r < n and s[r] == s[l]:
                indices = (l, r)
                r += 1
                l -= 1
                W = r - l + 1
            return indices, W

        maxLen = 0
        longest_indices = (0, 0)
        if n == 0: return ''
        for i in range(n):
            indices, W = expand(i, i, s)
            if W > maxLen:
                maxLen = W
                longest_indices = indices
            indices, W = expand(i, i + 1, s)
            if W > maxLen:
                maxLen = W
                longest_indices = indices
        start, end_inclusive = longest_indices
        
        return s[start: end_inclusive + 1]
        

        
        