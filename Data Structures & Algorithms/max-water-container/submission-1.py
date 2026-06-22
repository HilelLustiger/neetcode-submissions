class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        output = min(heights[left], heights[right]) * (right - left)

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            output = max(output, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        return output
            
