class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            if target > matrix[i][-1]:
                continue
            else:
                for j in range(c):
                    if matrix[i][j] == target:
                        return True
        return False