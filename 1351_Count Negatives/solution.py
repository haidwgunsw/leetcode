class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def BinarySearch(array):
            low = 0
            high = len(array) - 1
            while low <= high:
                mid = (low + high ) // 2
                if array[mid] < 0:
                    high = mid - 1
                elif array[mid] >= 0:
                    low = mid + 1
            return low

        result = 0
        for row in grid:
            result += len(row) - BinarySearch(row)
        return result
