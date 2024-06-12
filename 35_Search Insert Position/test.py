from solution import Solution

def run_tests():
    sol = Solution()
    
    # Test case 1
    nums1 = [1, 3, 5, 6]
    target1 = 5
    expected1 = 2
    result1 = sol.searchInsert(nums1, target1)
    print(f"Test case 1 - {'Passed' if result1 == expected1 else 'Failed'}: Expected {expected1}, Got {result1}")
    
    # Test case 2
    nums2 = [1, 3, 5, 6]
    target2 = 2
    expected2 = 1
    result2 = sol.searchInsert(nums2, target2)
    print(f"Test case 2 - {'Passed' if result2 == expected2 else 'Failed'}: Expected {expected2}, Got {result2}")
    
    # Test case 3
    nums3 = [1, 3, 5, 6]
    target3 = 7
    expected3 = 4
    result3 = sol.searchInsert(nums3, target3)
    print(f"Test case 3 - {'Passed' if result3 == expected3 else 'Failed'}: Expected {expected3}, Got {result3}")
    
    # Test case 4
    nums4 = [1, 3, 5, 6]
    target4 = 0
    expected4 = 0
    result4 = sol.searchInsert(nums4, target4)
    print(f"Test case 4 - {'Passed' if result4 == expected4 else 'Failed'}: Expected {expected4}, Got {result4}")
    
    # Test case 5
    nums5 = [1, 3, 5, 6]
    target5 = 4
    expected5 = 2
    result5 = sol.searchInsert(nums5, target5)
    print(f"Test case 5 - {'Passed' if result5 == expected5 else 'Failed'}: Expected {expected5}, Got {result5}")

if __name__ == "__main__":
    run_tests()
