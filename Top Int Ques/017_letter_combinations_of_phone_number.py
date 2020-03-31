class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits or digits == "1":
            return ""
        if len(digits) == 1 and int(digits[0]) == 1:
            return ""
        
        d = {'2':['a', 'b', 'c'],
             '3':['d', 'e', 'f'],
             '4':['g', 'h', 'i'],
             '5':['j', 'k', 'l'],
             '6':['m', 'n', 'o'],
             '7':['p', 'q', 'r', 's'],
             '8':['t', 'u', 'v'],
             '9':['w', 'x', 'y', 'z']}
        
        def backtrack(combo, nextdigits):
            if len(nextdigits) == 0:
                result.append(combo)
            else:
                for letter in d[nextdigits[0]]:
                    backtrack(combo + letter, nextdigits[1:])
                    
        result = []
        if digits != None:
            backtrack("", digits)
        return result
