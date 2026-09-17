class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
       
      
        while left <= right:
            if s[left] != s[right]:
                skipL = s[left+1:right+1]
                skipR = s[left:right]
                return self.isPalindrome(skipL) or self.isPalindrome(skipR)
            right -= 1
            left += 1
        return True
                    
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

        