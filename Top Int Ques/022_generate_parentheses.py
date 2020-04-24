class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(current, num_available, num_not_closed):
            if num_available == 0:
                return [current + ')'*num_not_closed]
            elif num_not_closed == 0:
                return helper(current + '(', 
                              num_available - 1,
                              num_not_closed + 1)
            else:
                return helper(current + '(',
                              num_available - 1,
                              num_not_closed + 1) + helper(current + ')',
                                                           num_available,
                                                           num_not_closed - 1)
                
        if n == 0:
            return []
        else:
            return helper('', n, 0)
