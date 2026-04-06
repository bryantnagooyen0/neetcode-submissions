class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        L = 0
        R = len(matrix) - 1
        while L < R:
            for i in range(R - L):
                top = L
                bottom = R

                #Topleft = matrix[top][L + i]
                #Topright = matrix[top + i][R]
                #Bottomleft = matrix[bottom - i][L]
                #Bottomright = matrix[bottom][R - i]

                #Save top left
                TopLeft = matrix[top][L + i]

                #Move bottom left into top left
                matrix[top][L + i] = matrix[bottom - i][L]

                #Move bottom right into bottom left
                matrix[bottom - i][L] = matrix[bottom][R - i]

                #Move top right into bottom right
                matrix[bottom][R - i] = matrix[top + i][R]

                #Move top left into top right
                matrix[top + i][R] = TopLeft
            L += 1
            R -= 1

        