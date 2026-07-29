class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        version1 = version1.split(".")
        version2 = version2.split(".")

        n = max(len(version1), len(version2))

        for i in range(n):
            if i < len(version1):
                a = int(version1[i])
            else:
                a = 0
            
            if i < len(version2):
                b = int(version2[i])
            else:
                b = 0

            if a < b:
                return -1
            elif a > b:
                return 1
        return 0    
        
