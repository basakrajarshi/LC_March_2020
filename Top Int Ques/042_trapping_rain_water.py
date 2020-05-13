class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == None:
            return 0
        
        left_highest = 0
        right_highest = 0
        left = 0
        right = len(height) - 1
        result = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_highest:
                    left_highest = height[left]
                else:
                    result += left_highest - height[left]
                left += 1
            else:
                if height[right] >= right_highest:
                    right_highest = height[right]
                else:
                    result += right_highest - height[right]
                right -= 1
        return result
