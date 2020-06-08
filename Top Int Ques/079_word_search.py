class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        columns = len(board[0])
           
        def backtrack(row, col, suffix):
            if len(suffix) == 0:
                return True
            
            if row < 0 or row == rows or col < 0 or col == columns \
            or board[row][col] != suffix[0]:
                return False
            
            ret = False
            
            board[row][col] = '#'
            
            for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ret = backtrack(row + rowOffset, 
                                col + colOffset, 
                                suffix[1:])
                if ret:
                    break
                    
            board[row][col] = suffix[0]
            
            return ret
        
        for row in range(rows):
            for col in range(columns):
                 if backtrack(row, col, word):
                        return True
