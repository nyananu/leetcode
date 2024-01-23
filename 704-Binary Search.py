# https://leetcode.com/problems/binary-search/

# APPROACH 1 - RECURSION

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        p_begin = 0
        p_end = len(nums) - 1

        return self.binary_search(nums, target, p_begin, p_end)


        
    def binary_search(self, nums, target, p_begin, p_end):
        if p_begin >= p_end:
            return -1
        
        p_mid = p_begin + ((p_end - p_begin)/2)
        
        if target == nums[p_mid]:
            return p_mid
        elif target < nums[p_mid]:
            p_end = p_mid - 1
            return self.binary_search(nums, target, p_begin, p_end)

        elif target > nums[p_mid]:
            p_begin = p_mid + 1
            return self.binary_search(nums, target, p_begin, p_end)




# APPROACH 2 - ITERATION

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        p_begin = 0
        p_end = len(nums) - 1


        # writing it this way to prevent number overflow incase of large numbers
        while p_begin <= p_end:
            p_mid = p_begin + ((p_end - p_begin)/2)

            if target == nums[p_mid]:
                return p_mid
            elif target < nums[p_mid]:
                p_end = p_mid - 1
            elif target > nums[p_mid]:
                p_begin = p_mid + 1

        return -1
