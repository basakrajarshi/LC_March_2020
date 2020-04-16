class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        
        result = 0

        num_to_str = str(x)
        num_to_str = num_to_str.rstrip('0')
        isneg = False
        if num_to_str[0] == '-':
            isneg = True
            num_to_str = num_to_str.lstrip('-')
  
        rev_str = num_to_str[::-1]
        str_to_num = int(rev_str)
        
        if isneg == False:
            result = str_to_num
        else:
            result = str_to_num - 2*(str_to_num)
        
        if result < (-2)**31 or result > (2)**31 - 1:
            return 0
        else:
            return result
