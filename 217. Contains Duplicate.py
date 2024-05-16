# https://leetcode.com/problems/contains-duplicate/

        # Approach 1: Map/Dict
        
       class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
        occurance_map = {}

        for i in nums:
            if i in occurance_map:
                return True
            else:
                occurance_map.update({ i: 1 })
        return False

        # Time Complexity: O(n) because map has constant time reads of O(1)
        # disadvantage: Space complexity is O(n) 


        # Approach 2: Set

        # numSet = set(nums)
            
        # if len(numSet) < len(nums):
        #     return True
        # return False

        # Time complexity: O(n) 
