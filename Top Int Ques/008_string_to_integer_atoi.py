class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        remove_spaces = str.lstrip(" ")
        if remove_spaces is None or len(remove_spaces) == 0:
            return 0
        
        isneg = False
        remove_sign = ''
        if remove_spaces[0] == '+':
            remove_sign = remove_spaces[1:]
        elif remove_spaces[0] == '-':
            remove_sign = remove_spaces[1:]
            isneg = True
        elif remove_spaces[0].isdigit() == False:
            return 0
        else:
            remove_sign = remove_spaces
            
        result = 0
        for char in remove_sign:
            if char.isdigit() == True:
                result = result*10 + int(char)
            else:
                break

        if isneg == True:
            if result > 2**31 - 1:
                return (-2)**31
            else:
                return (result - 2*result)
        else:
            if result > 2**31 - 1:
                return 2**31 - 1
            else:
                return result
