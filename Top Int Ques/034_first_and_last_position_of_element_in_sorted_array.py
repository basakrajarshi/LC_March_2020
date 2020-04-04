class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        starting = None
        ending = None
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                starting = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        if starting == None:
            return [-1, -1]
        
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                ending = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
                
        return [starting, ending]
