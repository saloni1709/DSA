class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(height) - 1

        max_area = 0

        while l < r:
            curr_area = (r-l) * min(height[l], height[r])
            max_area = max(max_area, curr_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area