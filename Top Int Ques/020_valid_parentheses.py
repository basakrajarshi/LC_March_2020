class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
        
        if len(s) % 2 != 0:
            return False
        
        d = {')':'(',
             '}':'{',
             ']':'['}
        
        stack = []
        
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack.pop() == d[char]:
                    continue
                else:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True
