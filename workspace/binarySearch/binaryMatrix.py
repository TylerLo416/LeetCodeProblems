class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl = 0
        rr = len(matrix)
        #check start and end of the current row of the matrix
        while rl <= rr:
            mid = (rl+rr)/2
            #if target is within these bounds, binary search this row
            if matrix[mid][len(matrix[0])-1] > target > matrix[mid][0]:
                l = 0
                r = len(matrix[0])
                while l <= r:
                    m = (l+r)/2
                    if matrix[mid][m] > target:
                        r = m-1
                    elif matrix[mid][m] < target:
                        l = m+1
                    elif matrix[mid][m] == target:
                        return True
                return False
            #else, binary search upwards or downwards
            elif target < matrix[mid][0]:
                rr = mid-1
            
            elif target > matrix[mid][len(matrix[0])-1]:
                rl = mid+1