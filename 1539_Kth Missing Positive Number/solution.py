class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right)//2
            if arr[mid] - mid - 1 < k:
                left = mid + 1
            else:
                right = mid
        return right + k