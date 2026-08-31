class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        if moves.count('L') == moves.count('R') and moves.count('D') == moves.count('U'):
            return True
        return False