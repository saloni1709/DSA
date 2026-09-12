class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        total = 0
        ans = []
        for i in nums:
            total += i
            ans.append(total)
        return ans