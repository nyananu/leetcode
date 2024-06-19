# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:

        # '(){}[]'
        stack = []
        
        for c in s:
            if (c == '('):
                stack.append(')')
            elif (c == '['):
                stack.append(']')
            elif (c == '{'):
                stack.append('}')
            elif (not stack or stack[-1] != c):
                return False
            else:
                stack.pop()

        return not(stack)


        # Time Complexity: O(n)
        # Space Complexity: O(n)
