class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        heads = [row[0] for row in matrix]
        l, r = 0, len(heads) - 1
        while l < r:
            mid = l + (r - l)//2
            if heads[mid] == target:
                return True
            if heads[mid] < target:
                l = mid
            else:
                r = mid - 1
        
        search_row = matrix[l]
        left, right = 0, len(search_row) - 1
        while left < right:
            mid = left + (right - left)//2
            if search_row[mid] == target:
                return True
            elif search_row[mid] < target:
                left = mid + 1
            else: 
                right = mid - 1
        return False