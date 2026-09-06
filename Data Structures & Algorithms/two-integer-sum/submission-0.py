class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HM = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in HM:
                return [HM[diff], i]
            HM[n] = i


        