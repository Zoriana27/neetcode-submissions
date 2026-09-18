class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k != len(nums):
            for i in range(k%len(nums)):
                temp = nums[-1]
                for j in range(len(nums)-1, -1, -1):
                    nums[j] = nums[j - 1]
                nums[0] = temp
        