class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        
        ans = []
        for word in title.split():
            if len(word) <= 2:
                ans.append(word.lower())
            else:
                ans.append(word.title())
        return " ".join(ans)