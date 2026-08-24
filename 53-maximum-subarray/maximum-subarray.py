class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        maxi = float('-inf')
        total = 0
        for i in range(0, n):
            total += nums[i]
            maxi = max(maxi, total)
            if total < 0:
                total = 0
        return maxi