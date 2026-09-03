class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        v1 = version1.split(".")
        v2 = version2.split(".")
        v = max(len(v1), len(v2))

        for i in range(v):
            if len(v1) > i:
                a = int(v1[i])
            else:
                a = 0
            
            if len(v2) > i:
                b = int(v2[i])
            else:
                b = 0

            if a < b:
                return -1
            elif a > b:
                return 1
        return 0