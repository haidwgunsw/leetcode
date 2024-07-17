class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for f in counter.values():
            if f > 2:
                return False
        return True
    
#time complexity: O(n)
# if I didn't come across the solution, I would have done this

# use Counter to make a dictionary of the frequency of each number
# then iterate through the values of the dictionary

# if the frequency of any number is greater than 2
# meaning there are more than 2 of the same number
# then it's impossible to split the array with distinct numbers

# else, it's possible to split the array with distinct numbers