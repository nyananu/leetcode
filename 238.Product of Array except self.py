class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #            [1,  2,  3, 4]
        # prefix:      [1,  1,  2, 6]
        # suffix:     [24, 12, 4, 1]
        # output:    [24, 12, 8, 6]

        n = len(nums)
        answer = [1] * n
        
        # Calculate the prefix product for each element and store it in answer
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Calculate the suffix product for each element and multiply it to answer
        suffix = 1
        for i in reversed(range(n)):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
        
      
