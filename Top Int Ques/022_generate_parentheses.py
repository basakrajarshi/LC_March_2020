class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def helper(curr, num_available, num_not_closed):
            if num_available == 0:
                return [curr + ')'*num_not_closed]
            elif num_not_closed == 0:
                return helper(curr + '(', num_available - 1, num_not_closed + 1)
            else: 
                return helper(
                curr + '(', num_available - 1, num_not_closed + 1
            ) + helper(
                curr + ')', num_available, num_not_closed - 1
            )
        
        if n == 0:
            return []
        else:
            return helper('', n, 0)
