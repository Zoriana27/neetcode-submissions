class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[0]
        firstVal = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif firstVal <= nums[mid]:
                left = mid + 1
                firstVal = nums[left]
            else:
                right = mid - 1
        return nums[0]

