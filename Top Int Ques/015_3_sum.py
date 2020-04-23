class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # Sort the array in ascending order
        nums.sort()
        
        # Go through all numbers in the array except the last two
        for i in range(len(nums) - 2):
            
            # Move forward if the first index (i) has duplicate values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Create second index
            left = i + 1
            
            # Create third index
            right = len(nums) - 1
            
            # While second index is less than third index
            while left < right:
                
                # Find the sum of the three numbers
                total = nums[i] + nums[left] + nums[right]
                
                # If sum < 0, increase left index
                if total < 0:
                    left += 1
                
                # If sum > 0, decrease right index
                elif total > 0:
                    right -= 1
                
                # If sum = 0, add the triplet to results
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # Skip duplicates found through second index
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates found through third index
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Increase both left and right index since sum found
                    left += 1
                    right -= 1
                    
        return result                 
