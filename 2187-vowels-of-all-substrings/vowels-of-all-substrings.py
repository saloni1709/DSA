class Solution(object):
    def countVowels(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        count = 0
        vowel = 0
        for i in range(len(word)):
            if word[i] in 'aeiou':
                vowel += i+1
            count += vowel
        return count