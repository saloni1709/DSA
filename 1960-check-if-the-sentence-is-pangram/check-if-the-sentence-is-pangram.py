class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
        alpha = "abcdefghijklmnopqrstuvwxyz"

        for ch in alpha:
            if ch not in sentence:
                return False
        return True