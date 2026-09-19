class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False
            
        # Step 1: Binary search to find the correct row
        top, bottom = 0, len(matrix) - 1
        target_row = -1
        
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                target_row = mid
                break
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                top = mid + 1
                
        if target_row == -1:
            return False
            
        # Step 2: Binary search within the selected row
        row = matrix[target_row]
        left, right = 0, len(row) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
