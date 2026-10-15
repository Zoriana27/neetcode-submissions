class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = 1
        curr_min = 1
        max_so_far = float('-inf')
        
        for num in nums:
            if num < 0:
                # Swap min and max because multiplying by a negative flips their signs
                curr_max, curr_min = curr_min, curr_max
            
            # Decide whether to extend the current product or start fresh at num
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)
            
            max_so_far = max(max_so_far, curr_max)
            
        return max_so_far