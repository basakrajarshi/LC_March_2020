class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        rowbegin = 0
        rowend = len(matrix)
        columnbegin = 0
        columnend = len(matrix[0])
        result = []
        
        while rowend > rowbegin and columnend > columnbegin:
            for i in range(columnbegin, columnend):
                result.append(matrix[rowbegin][i])
                
            for j in range(rowbegin + 1, rowend - 1):
                result.append(matrix[j][columnend-1])
                
            if rowbegin + 1 != rowend:
                for i in range(columnend - 1, columnbegin - 1, -1):
                    result.append(matrix[rowend - 1][i])
                    
            if columnbegin + 1 != columnend:
                for j in range(rowend - 2, rowbegin, -1):
                    result.append(matrix[j][columnbegin])
                    
            rowbegin += 1
            rowend -= 1
            columnbegin += 1
            columnend -=1 
            
        return result
