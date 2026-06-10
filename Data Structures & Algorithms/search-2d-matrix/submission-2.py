class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l, r = 0, r*c-1

        while l <= r:
            mid = (l+r)//2
            row = mid//c
            col = mid%c
            v = matrix[row][col]

            if v == target:
                return True
            elif v < target:
                l=mid+1
            else:
                r=mid-1
        return False
        
