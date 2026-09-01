class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        word = s.split()[::-1]
        return " ".join(word)