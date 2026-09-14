class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
         
        def dfs(i, currentCombo, total):
            if total == target:
                result.append(currentCombo.copy())
                return
            if i >= len(nums) or total > target:
                return
            currentCombo.append(nums[i])
            dfs(i, currentCombo, total + nums[i])
            currentCombo.pop()
            dfs(i + 1, currentCombo, total)
        dfs(0, [], 0)
        return result


        