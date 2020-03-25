class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        median = 0.0
        middle_val = (len(nums) + 1)//2
        
        if len(nums)%2 == 0:
            median = (nums[middle_val - 1] + nums[middle_val])/2.0
        else:
            median = nums[middle_val - 1]
            
        return median
