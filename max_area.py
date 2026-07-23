## Container With Most Water
class Solution:
    def max_area(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_area = 0
        while l < r:
            # Multiply the lowest of the two heights by the distance b/t them
            area = min(heights[l], heights[r]) * (r-l)
            max_area = max(max_area, area)

            # Update one of the indices
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return max_area
