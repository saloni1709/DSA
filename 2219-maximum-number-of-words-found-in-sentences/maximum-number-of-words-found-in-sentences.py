class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        
        maximum = 0

        for sentence in sentences:
            words = sentence.split()

            count = len(words)

            if count > maximum:
                maximum = count
        
        return maximum
