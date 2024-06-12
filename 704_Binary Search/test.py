from solution import Solution

def run_tests():
    sol = Solution()
    
    # Test case 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    expected1 = 4
    result1 = sol.search(nums1, target1)
    print(f"Test case 1 - {'Passed' if result1 == expected1 else 'Failed'}: Expected {expected1}, Got {result1}")
    
    # Test case 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    expected2 = -1
    result2 = sol.search(nums2, target2)
    print(f"Test case 2 - {'Passed' if result2 == expected2 else 'Failed'}: Expected {expected2}, Got {result2}")
    
    # You can add more test cases as needed
    # Test case 3
    nums3 = []
    target3 = 1
    expected3 = -1
    result3 = sol.search(nums3, target3)
    print(f"Test case 3 - {'Passed' if result3 == expected3 else 'Failed'}: Expected {expected3}, Got {result3}")
    
    # Test case 4
    nums4 = [5]
    target4 = 5
    expected4 = 0
    result4 = sol.search(nums4, target4)
    print(f"Test case 4 - {'Passed' if result4 == expected4 else 'Failed'}: Expected {expected4}, Got {result4}")
    
if __name__ == "__main__":
    run_tests()
