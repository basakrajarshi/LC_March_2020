class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d  = {}
        # Go through each word in strs
        for s in strs:
            # Sort the characters of the string
            # and store in a new string
            sorted_char = ''.join(sorted(s))
            # If this sorted string is not in the dictionary
            if sorted_char not in d:
                # Store the characters as list of characters in key of dict
                # Store the word as the value for the corresponding key
                d[sorted_char] = [s]
            else:
                # Store the word corresponding to the list in keys that
                # contains the same characters
                d[sorted_char].append(s)        
        
        result = []
        for value in d.values():
            result.append(value)

        return result
