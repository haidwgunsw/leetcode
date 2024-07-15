class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary search for the square root of the number
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        
        # If we haven't found the square root, the number is not a perfect square
        return right