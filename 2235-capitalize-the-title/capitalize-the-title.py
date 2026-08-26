class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        
        ans = []

        for i in title.split():
            if len(i) <= 2:
                ans.append(i.lower())
            else:
                ans.append(i.title())
        return " ".join(ans)