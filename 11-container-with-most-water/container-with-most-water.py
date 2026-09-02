class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(height) - 1
        max_len = 0
        while l < r:
            curr_len = (r-l) * min(height[l], height[r])
            max_len = max(max_len, curr_len)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_len