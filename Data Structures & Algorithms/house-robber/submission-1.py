class Solution:
    def rob(self, nums: List[int]) -> int:
        #Top Down recursive memoisation
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        memo = {0: nums[0], 1: max(nums[0], nums[1])}
        def helper(i):
            if i in memo:
                return memo[i]
            else:
                memo[i] = max(helper(i-1), helper(i-2) + nums[i])
                return memo[i]
        return helper(len(nums)-1)