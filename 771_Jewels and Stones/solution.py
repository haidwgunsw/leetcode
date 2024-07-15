class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels) # if not set, time complexity will be O(j*s)
        count = 0
        for s in stones:
            if s in jewels:
                count += 1

        return count
    
# time complexity: O(j+s)