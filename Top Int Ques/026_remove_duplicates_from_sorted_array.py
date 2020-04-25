class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        # Initialize an index for iterating
        i = 0
        # Initialize an index to track length of array
        l = len(nums)
        
        # Loop through all elements
        while i < l:
            # Delete adajcent elements that are identical
            if nums[i] == nums[i+1]:
                del nums[i+1]
                # Update length of array
                l = len(nums)
            # Increase index when not identical    
            else:
                i += 1
            # Break out of loop if we have reached the last element
            if i == l - 1:
                break
        return len(nums)
