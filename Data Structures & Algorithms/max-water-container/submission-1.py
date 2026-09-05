# O(n^2)
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        p1 = 0
        p2 = len(heights)-1

        while(p1 != p2):
            area = (p2 - p1) * min(heights[p1], heights[p2])
            
            if(area > max):
                max = area
                continue
            
            elif(heights[p1] < heights[p2]):
                p1 += 1
            else:
                p2 -= 1
        return max
        