class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        for i in alpha:
            if i not in sentence:
                return False
        return True