class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            start, end = 0, len(row) - 1
            if target > row[end]:
                continue
            while start <= end:
                mid = (start + end) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        return False
        