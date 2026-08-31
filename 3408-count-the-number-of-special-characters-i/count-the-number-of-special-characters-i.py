class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """

        count = 0
        for i in set(word):
            if i.islower() and i.upper() in word:
                count += 1
            # else:
            #     count = 0
        return count