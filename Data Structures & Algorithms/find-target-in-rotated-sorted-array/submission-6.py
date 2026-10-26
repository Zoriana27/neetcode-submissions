class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def findBreakingPoint():
        
            left, right = 0, len(nums) - 1
            
            # If array is already fully sorted
            if nums[left] <= nums[right]:
                return right

            while left <= right:
                mid = (left + right) // 2
                
                # Check bounds before comparing with mid + 1
                if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                    return mid
                
                # Check if left half is sorted (using fixed nums[0] reference)
                if nums[0] <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return len(nums) - 1
        
        def binarySearch(left, right):
            while left <= right:
                mid = (left + right)//2
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        breakingPointIndex = findBreakingPoint()
        if target >= nums[0]:
            left = 0
            right = breakingPointIndex
            return binarySearch(left, right)
        else:
            left = breakingPointIndex + 1
            right = len(nums) - 1
            return binarySearch(left, right)
        