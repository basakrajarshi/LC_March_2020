class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Get the substring to check for palindromic
        # starting from the letter(s)
        # and return the length of the palindrome
        def expand(s, l, r):
            while (l >= 0 and r <= len(s) - 1 and s[r] == s[l]):
                l -= 1
                r += 1
            return r - l - 1
        
        if s == None or len(s) < 1:
            return ''
        
        start = 0
        end = 0
        
        # Starting with each letter in the string
        for i in range(len(s)):
            # Get the length of the largest odd length palindrome
            len1 = expand(s, i, i)
            # Get the length of the largest even length palindrome
            len2 = expand(s, i, i+1)
            maxl = max(len1, len2)
            # Check if new palindrome is longer than previous largest
            if maxl > end - start:
                start = i - (maxl - 1)//2
                end = i + (maxl)//2
        
        return s[start:end+1]
