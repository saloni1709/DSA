class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """

        max = 0

        for sentence in sentences:
            word = sentence.split()
            if len(word) > max:
                max = len(word)
        
        return max
        
        
