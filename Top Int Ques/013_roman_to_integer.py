class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0:
            return 0
        
        d = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}
        
        result = 0
        
        i = 0
        while i < len(s):
            
            val1 = d[s[i]]
            if i < len(s) - 1:
                val2 = d[s[i+1]]
                
                if val1 >= val2:
                    result = result + val1
                    i += 1
                else:
                    result = result + val2 - val1
                    i += 2
                    
            else:
                result = result + val1
                i += 1
            
        return result    
