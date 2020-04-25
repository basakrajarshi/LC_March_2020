class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        if dividend == (-2)**31 and dividend == 1:
            return dividend
        if dividend == (-2)**31 and divisor == -1:
            return (2**31 - 1)
        if dividend < (-2)**31 or dividend > 2**31 - 1:
            if abs(divisor) == 1:
                return 2**31 - 1
    
        if dividend > 0 and divisor > 0 and dividend < divisor:
            return 0
        
        if divisor == dividend:
            return 1
        if divisor == dividend * (-1):
            return -1
        if divisor == 1:
            return dividend
        if divisor == -1:
            if dividend < 0:
                return abs(dividend)
            elif dividend > 0:
                return dividend - 2*dividend
            else:
                return 0
        if dividend == 0:
            return 0
        
        isneg_dividend = False
        isneg_divisor = False
        
        if dividend < 0:
            isneg_dividend = True
        if divisor < 0:
            isneg_divisor = True
            
        mod_dividend = abs(dividend)
        mod_divisor = abs(divisor)
        
        count = 1
        new_divisor = mod_divisor
        while new_divisor <= mod_dividend:
            new_divisor += mod_divisor
            count += 1
            
            if new_divisor + mod_divisor > mod_dividend:
                break
        
        if count > 2**31 - 1:
            return 2**31 - 1
        
        if isneg_dividend == True and isneg_divisor == True:
            return count
        elif isneg_dividend == True and isneg_divisor == False:
            return count - 2*count
        elif isneg_dividend == False and isneg_divisor == True:
            return count - 2*count
        else:
            return count
