# https://leetcode.com/problems/contains-duplicate/

        # Approach 1: Map/Dict
        
       class Solution:
        def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = {}

        for i in nums:
            if (i not in freq_map):
                freq_map[i] = 1
            else:
                return True
        return False

        # Time Complexity: O(n) because map has constant time reads of O(1)
        # disadvantage: Space complexity is O(n) 


        # Approach 2: Set

        # numSet = set(nums)
            
        # if len(numSet) < len(nums):
        #     return True
        # return False

        # Time complexity: O(n) 
