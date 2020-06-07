class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums or len(nums) == 0:
            return []
        
        n = len(nums)
        power_set_size = 2**n
        
        results = []
        
        for i in range(0, power_set_size):
            result = []
            for j in range(0, n):
                if ((i & (1 << j)) > 0):
                    result.append(nums[j])
            results.append(result)
            
        return results
