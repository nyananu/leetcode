# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create map to have key as curr, and index as val
        # go through map to see what is target - num, and get its corresponding index
        
        num_map = {}

        # whenever we want to keep track of index as well, we use enumerate
        for i, n in enumerate(nums):
            diff = target - n
        
        # if the diff is in the map, get the index of the curr (num_map[diff]) and the current index
            if diff not in num_map:
                num_map[n] = i
            else:
                return [num_map[diff], i]
