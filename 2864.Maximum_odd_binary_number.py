# https://leetcode.com/problems/maximum-odd-binary-number/description/
# Brute Force: Sorting required so runtime is O(n log n)

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # sort and reverse string
        res = sorted(s, reverse=True)

        # loop through to change the last 1 to 0, and last 0 to 1 - to make it odd
        for i in range(len(res)):
            if res[i] != '1':
                res[i - 1] = '0'
                res[-1] = '1'
                break
        
        return ''.join(res)





        
