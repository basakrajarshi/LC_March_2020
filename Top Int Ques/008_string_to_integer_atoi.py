class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        stripped = str.lstrip(" ")
        if stripped == '':
            return 0
        negative = False
        remove_neg = None
        if stripped[0] == '-':
            negative = True
            remove_neg = stripped[1:]
        elif stripped[0] == '+':
            remove_neg = stripped[1:]
        if remove_neg is not None:
            if remove_neg == '':
                return 0
            if remove_neg[0].isdigit() == False:
                return 0
        else:
            remove_neg = stripped
        remove_char = ''
        for char in remove_neg:
            if char.isdigit() == True:
                remove_char = remove_char + char
            else:
                break
        result = 0
        for char in remove_char:
            result = 10*result + int(char)
        if result > (2)**31-1:
            if negative == True:
                return (-2)**31
            else:
                return (2)**31 - 1
        else:
            if negative == True:
                return result - 2*result
            else:
                return result
