class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = 0
        maxi = float('-inf')
        for i in range(0, len(nums)):
            total += nums[i]
            maxi = max(maxi, total)

            if total < 0:
                total = 0
        return maxi