class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (high + low) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
            
        if high >= 0:
            left, right = 0, len(matrix[0]) - 1

            while left <= right:
                mid = (left + right) // 2
                if target == matrix[high][mid]:
                    return True
                elif target < matrix[high][mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return False