class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,cols = len(matrix), len(matrix[0])
        s,e = 0, row*cols-1
        mid = s+(e-s)//2
        while s <= e:
            ele = matrix[mid//cols][mid % cols]

            if ele == target:
                return True
            elif ele < target:
                s = mid+1
            else:
                e = mid - 1
            mid = s+(e-s)//2
        return False