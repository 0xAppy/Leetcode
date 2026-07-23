class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(i+1,rows):
                matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        
        for row in matrix:
            row.reverse()
        