class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(1, n+1):
            nums.append(i)
        res = []
        combo = []
        def backtrack(i):
            if len(combo) == k:
                res.append(combo.copy())
                return
            
            if i == len(nums):
                return
            
            #don't include nums[i]
            backtrack(i + 1)

            #include nums[i]
            combo.append(nums[i])
            backtrack(i + 1)
            combo.pop()
        backtrack(0)
        return res