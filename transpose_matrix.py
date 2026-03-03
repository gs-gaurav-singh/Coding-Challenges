class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        transpose = [[r[col] for r in matrix] for col in range(len(matrix[0]))]
        return transpose
