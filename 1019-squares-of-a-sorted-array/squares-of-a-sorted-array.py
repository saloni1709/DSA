class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        l = []

        for i in nums:
            i = i**2
            l.append(i)
        l.sort()
        
        return l

     
            
        