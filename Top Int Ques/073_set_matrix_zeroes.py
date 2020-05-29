class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeroes = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeroes.append([i,j])
        
        for zero in zeroes:
            for i in range(len(matrix[0])):
                matrix[zero[0]][i] = 0
            for j in range(len(matrix)):
                matrix[j][zero[1]] = 0
            
        return matrix
