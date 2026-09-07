class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximumArea = 0
        
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            smallerHeight = min(heights[l], heights[r])
            area = width * smallerHeight
            maximumArea = max(maximumArea, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maximumArea

            

        