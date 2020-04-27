class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize result
        result = 1
        # Set flag for running while loop
        flag = 0
        
        while flag == 0:
            # If the result is not in nums, return it
            if result not in nums:
                return result
            # Otherwise increment result by 1
            else:
                result += 1
