class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        
        def get_compliment(c):
            if c == ')':
                return '('
            if c == '}':
                return '{'
            if c == ']':
                return '['
        
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                check = get_compliment(char)
                item = stack.pop()
                if item != check:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False
