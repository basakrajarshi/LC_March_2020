class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        leng = len(matrix[0])
        
        for layer in range (0, leng//2):
            f = layer
            l = leng - layer - 1
            for i in range (f,l):
                offset = i - f
                top = matrix[f][i]
                matrix[f][i] = matrix[l - offset][f]
                matrix[l - offset][f] = matrix[l][l - offset]
                matrix[l][l - offset] = matrix[i][l]
                matrix[i][l] = top
                
        return matrix
