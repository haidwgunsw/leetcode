class Solution:
    def arrangeCoins(self, n: int) -> int:
        # Initialize pointers to first and last possible row lengths
        left, right = 1, n
        
        while left <= right:
            # Compute the midpoint between left and right
            mid = left + (right - left) // 2
            
            # Compute the total number of coins needed for mid complete rows
            coins = (mid * (mid + 1)) // 2
            
            # If we have enough coins, look for a smaller number of rows
            if coins <= n:
                left = mid + 1
            # Otherwise, look for a larger number of rows
            else:
                right = mid - 1
                
        # Return the number of complete rows (i.e., right pointer)
        return right
    
# Time complexity: O(log(n))

# the idea behind binary search
# to find the largest number meaning to find the right pointer
# the right pointer will stop at the largest number in binary search
# so it's the number of complete rows

# the formula for the sum of the first n natural numbers is n(n+1)/2