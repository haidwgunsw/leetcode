class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# Time complexity: O(log(n))
# in this question, the time complexity is O(log(n)) because we are reducing the search space by half every time.

# i was dumb enough to not realize the solution is actually this simple
# basically just check if the string representation of the number is the same as its reverse
# if it is, then it's a palindrome