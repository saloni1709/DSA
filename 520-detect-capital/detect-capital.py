class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if word.isupper() or word.islower() or word == word.capitalize():
            return True
        return False