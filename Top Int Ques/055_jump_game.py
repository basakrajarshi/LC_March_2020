class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        jumps = [0] * n
        
        if n == 0:
            return False
        
        if nums[0] == 0 and n >= 2:
            return False
        
        jumps[0] = 0
        
        for i in range(1, n):
            jumps[i] = float('inf')
            for j in range(i):
                if i <= j + nums[j] and jumps[j] != float('inf'):
                    jumps[i] = min(jumps[i], jumps[j] + 1)
                    break
                    
        if jumps[n-1] != float('inf'):
            return True
        else:
            return False
