class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        '''if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)'''
        
        d = [[1 for i in range(n)] for j in range(m)]
        
        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]
                
        return d[m - 1][n - 1]
