class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        row, col = 0, len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            current = matrix[row][col]
            if current == target:
                return True
            elif current < target:
                row += 1 
            else:
                col -= 1  
        
        return False