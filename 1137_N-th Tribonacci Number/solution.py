class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        one_before = 1
        two_before = 1
        three_before = 0
        total = 0
        for i in range(3, n+1): #py exclude last
            total = one_before + two_before + three_before
            three_before = two_before
            two_before = one_before
            one_before = total
        return total