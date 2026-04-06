class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        We set boundaries to be outside of matrix and squares we have already traversed through
        """
        squares = len(matrix) * len(matrix[0])
        result = []
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        top = 0
        
        while len(result) < squares:
            row = top
            col = left
            result.append(matrix[row][col])
            
            while col < right and len(result) < squares:
                col += 1
                result.append(matrix[row][col])
                
            while row < bottom and len(result) < squares:
                row += 1
                result.append(matrix[row][col])

            while col > left and len(result) < squares:
                col -= 1
                result.append(matrix[row][col])

            while row > top + 1 and len(result) < squares:
                row -= 1
                result.append(matrix[row][col])
            left += 1
            right -= 1
            bottom -= 1
            top += 1
        return result

