# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       # Option 1

         for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target) and (i != j):
                    return([i,j])

# Time Complexity: O(n^2)
# Space Complexity: O(1)

xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    # Option 2

        index_map = {}

        for i in range(len(nums)):
            x = target - nums[i] 
            if (x in index_map): 
                return([index_map[x], i])
            index_map[nums[i]] = i

# Time Complexity: O(n)
# Space Complexity: O(n)

