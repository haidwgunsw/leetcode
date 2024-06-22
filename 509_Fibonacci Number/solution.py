class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        one_before = 1
        two_before = 0
        total = 0
        for i in range(2, n+1): #py exclude last
            total = one_before + two_before
            two_before = one_before
            one_before = total
        return total