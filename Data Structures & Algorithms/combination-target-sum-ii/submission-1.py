class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combo = []
        candidates.sort()
        

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(combo.copy())
                return
            if i == len(candidates) or curr_sum > target:
                return
            #include candidates[i]
            combo.append(candidates[i])
            backtrack(i+1, curr_sum + candidates[i])
            combo.pop()
            #don't include candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, curr_sum)
        backtrack(0, 0)
        return res
        