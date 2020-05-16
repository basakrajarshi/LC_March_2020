class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0:
            return 1
        
        if n == 1 or x == 1:
            return x
        
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        
        isneg = False
        if n < 0:
            isneg = True
        elif n > 0:
            isneg = False

        
        n = abs(n)
        
        res = 1.0
        i = 0
        while i < n:
            res = res * x
            i += 1
        #print(result)
        if isneg == False:
            result = res
        else:
            result = 1/res
            
        return result
