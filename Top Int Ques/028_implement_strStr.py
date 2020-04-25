class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None or len(needle) == 0:
            return 0
        
        len_n = len(needle)
        len_h = len(haystack)
        
        if len_h < len_n:
            return -1
        
        for i in range(len_h - len_n + 1):
            if haystack[i : i + len_n] == needle:
                return i
        return -1
