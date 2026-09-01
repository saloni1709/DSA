class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        for i in nums:
            i **= 2
            ans.append(i)
            ans.sort()
        return ans