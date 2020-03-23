class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = ''
        length = 0
        for char in s:
            if char not in result:
                result = result + char
            else:
                result = result[result.index(char)+1:] + char
            length = max(len(result), length)
        return length
