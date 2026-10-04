class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        permutation = []

        def backtrack():
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return
            
            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    backtrack()
                    permutation.pop()
        
        backtrack()
        return result

        