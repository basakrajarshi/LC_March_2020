class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = nums[0]
        maximum_sum = nums[0]
        
        n = len(nums)
        
        for i in range(1, n):
            current_sum = max(nums[i], current_sum + nums[i])
            maximum_sum = max(current_sum, maximum_sum)
            
        return maximum_sum
