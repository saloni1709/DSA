class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        # moves.count("U")
        # moves.count("D")
        # moves.count("L")
        # moves.count("R")

        if moves.count("L") == moves.count("R") and moves.count("U") == moves.count("D"):
            return True
        else:
            return False