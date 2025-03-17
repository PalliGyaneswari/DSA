class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Start from the top-right corner
        row, col = 0, len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            current = matrix[row][col]
            if current == target:
                return True
            elif current < target:
                row += 1  # Move down
            else:
                col -= 1  # Move left
        
        return False