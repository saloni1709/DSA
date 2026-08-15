class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = row * col - 1

        while l <= r:
            mid = (l + r) // 2
            row_index = mid // col
            col_index = mid % col
            value = matrix[row_index][col_index]

            if value == target:
                return True
            elif value < target:
                l = mid + 1
            elif value > target:
                r = mid - 1
        return False