class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        isneg = False
        if dividend == 0:
            return 0
        elif divisor == dividend:
            result = 1
        elif divisor == 1:
            result = dividend
        elif divisor == -1:
            if dividend < 0:
                result =  abs(dividend)
            else:
                result = (dividend - 2*dividend)
        else:
            
            if divisor < 0 and dividend > 0:
                isneg = True
            elif divisor > 0 and dividend < 0:
                isneg = True
            divisor = abs(divisor)
            dividend = abs(dividend)
            result = 0
            counter = 0
            while counter < dividend:
                counter += divisor
                if counter <= dividend:
                    result += 1
            #print(result)
            
        if isneg == True:
            result = result - 2*result

        if result < (-2)**31 or result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result
