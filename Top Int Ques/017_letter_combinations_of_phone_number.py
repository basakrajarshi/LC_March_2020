class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == None or len(digits) == 0 or digits == '1':
            return []
        
        # Define dictionary for storing all letters
        d = {'1' : [],
             '2' : ['a', 'b', 'c'],
             '3' : ['d', 'e', 'f'],
             '4' : ['g', 'h', 'i'],
             '5' : ['j', 'k', 'l'],
             '6' : ['m', 'n', 'o'],
             '7' : ['p', 'q', 'r', 's'],
             '8' : ['t', 'u', 'v'],
             '9' : ['w', 'x', 'y', 'z']}
        
        # Recursive function with letter string and string of digits: params
        def backtrack(combo, nextdigits):
            # If have no more digits left
            if len(nextdigits) == 0:
                # Add the string to results
                result.append(combo)
            else:
                # For each letter belonging to the first digit in the string
                for letter in d[nextdigits[0]]:
                    # Recursuvely call the backtrack function 
                    # with updated letter string and 
                    # updates string of digits
                    backtrack(combo + letter, nextdigits[1:])
                
        result = []
        backtrack("", digits)
        
        return result
