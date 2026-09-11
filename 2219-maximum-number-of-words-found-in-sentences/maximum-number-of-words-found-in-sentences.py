class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        
        max = 0
        for i in sentences:
            word = i.split()
            if len(word) > max:
                max = len(word)
        return max