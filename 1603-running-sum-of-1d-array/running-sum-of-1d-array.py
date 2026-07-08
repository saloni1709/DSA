class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        sum = 0
        ans = []
        for i in nums:
            sum+=i
            ans.append(sum)
        return ans
