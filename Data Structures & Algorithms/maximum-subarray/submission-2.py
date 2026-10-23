class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0] #-2
        maxSum = nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in range(1, len(nums)):
            currSum = max(nums[i], currSum + nums[i]) #max(-1, -3) = -1
            maxSum = max(maxSum, currSum)
        
        return maxSum

        