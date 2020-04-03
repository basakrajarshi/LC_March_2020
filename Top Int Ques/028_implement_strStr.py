class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        
        if needle in haystack:
                ind = haystack.index(needle)
                return ind
        else:
            return -1
