class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        l = 0
        r = len(height) - 1

        max_l = 0
        max_r = 0

        water = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] > max_l:
                    max_l = height[l]   
                else:            
                    water += max_l - height[l]
                l += 1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    water += max_r - height[r]
                r -= 1
        
        return water