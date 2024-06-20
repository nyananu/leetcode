# https://leetcode.com/problems/valid-palindrome/submissions/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert all uppercase to lowercase and remove space
        # remove all non-alphanumeric chars
        # have a ptr at beginning and another at end of string, and compare, coming in towards the middle

        clean_s = s.replace(' ', '').lower()
        clean_s = ''.join(c for c in clean_s if c.isalnum())

        left = 0
        right = len(clean_s) - 1

        while left < right:
            if (clean_s[left] != clean_s[right]):
                return False
            left += 1
            right -= 1
        
        return True
        

        
