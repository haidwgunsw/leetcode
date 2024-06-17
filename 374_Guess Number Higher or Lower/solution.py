# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right)//2
            result = guess(mid)

            if result == 0: #correct guess
                return mid
            elif result < 0:
                right = mid - 1 
            else:
                left = mid + 1
        return -1
        

#i had a hard time solving this problem because i was not able to understand the problem statement properly.