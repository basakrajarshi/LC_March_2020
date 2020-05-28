class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0 or x == 1:
            return x
    
        result = 2
        while result * result <= x: 
            if result**2 == x:
                return result
            result += 1
            
        return result - 1
