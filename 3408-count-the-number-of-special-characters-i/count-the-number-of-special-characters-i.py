class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        count = 0
        word = set(word)
        for i in word:
            if i.isupper() and i.lower() in word:
                count += 1
        
        return count