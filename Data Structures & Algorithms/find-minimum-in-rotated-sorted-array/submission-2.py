class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minimum = float('inf')
        
        while left <= right:
            if nums[left] < nums[right]:
                minimum = min(nums[left], minimum)
                break
            mid = (left + right) // 2
            minimum = min(nums[mid], minimum)
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return minimum
            
        