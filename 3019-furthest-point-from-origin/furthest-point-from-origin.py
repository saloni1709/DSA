class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        
        l = 0
        r = 0
        blank = 0

        for i in moves:
            if i == 'L':
                l += 1
            elif i == 'R':
                r += 1
            else:
                blank += 1
        
        return abs(l-r) + blank 