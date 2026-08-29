class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        count = 0
        l = 0
        for r in range(len(word)):
            sub = word[l:r+1]
            if word[r] in 'aeiou':
                count += (r + 1) * (len(word) - r)
        return count  