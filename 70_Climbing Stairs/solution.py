class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return climb(n-1) + climb(n-2) 
        # take O(2^n) time

        # bottom-up 1-1-2-3-5-8 => O(n) fib sequence

        if n == 1:
            return 1
        one_before = 1
        two_before = 1
        total = 0
        for i in range(2, n+1): #py exclude last
            total = one_before + two_before
            two_before = one_before
            one_before = total
        return total


        