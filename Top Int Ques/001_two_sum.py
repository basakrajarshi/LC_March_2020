class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for n in range(0, len(nums)):
            if target - nums[n] not in d:
                d[nums[n]] = n
            else:
                return (d[target - nums[n]], n)
