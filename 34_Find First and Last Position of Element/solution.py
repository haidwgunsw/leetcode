class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = self.binarySearch(nums,target,True)
        right = self.binarySearch(nums,target,False)
        return [left,right]

    # leftBias = True/False. If False, res is rightBiased:
    def binarySearch(self,nums,target,leftBias):
        left = 0
        right = len(nums) - 1
        i = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                i = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        return i
        
        