class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        
        s = "".join(word1)
        s1 = "".join(word2)

        if s == s1:
            return True
        else:
            return False
        