class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # Function for generating next sequence
        # given the previous sequence
        def next_number(s):
            i = 0
            result = []
            # Go thorugh each number in the sequence
            while i < len(s):
                # Inititialize count to 1
                count = 1
                # Check if adjacent numbers are the same
                # Until the end of the string
                while i < len(s) - 1 and s[i] == s[i+1]:
                    # Increment iterator and count
                    i += 1
                    count += 1
                # Append the count and the number (both as strings)
                # to the result 
                result.append(str(count) + s[i])
                # Increment iterator
                i += 1
            # Return result after converting to string
            return ''.join(result)
        
        
        s = "1"
        for i in range(n-1):
            s = next_number(s)
            
        return s
