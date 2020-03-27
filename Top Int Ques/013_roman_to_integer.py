class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        def get_integer_value(x):
            if x == 'I':
                return 1
            if x == 'V':
                return 5
            if x == 'X':
                return 10
            if x == 'L':
                return 50
            if x == 'C':
                return 100
            if x == 'D':
                return 500
            if x == 'M':
                return 1000
        
        result = 0
        i = 0 
        while i < len(s):
            s1 = get_integer_value(s[i])
            
            if i+1 < len(s):
                s2 = get_integer_value(s[i+1])
                
                if s1 >= s2:
                    result = result + s1
                    i += 1
                else:
                    result = result + s2 - s1
                    i += 2
            
            else:
                result = result + s1
                i += 1
                
        return result
