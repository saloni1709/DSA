class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()

        if len(nums) == 0:
            return 0
        
        ans = 1
        count = 1

        i = 0
        
        for j in range(i+1, len(nums)):
            if nums[j] - nums[j-1] == 1:
                count += 1
                ans = max(ans, count)
            elif nums[j] == nums[j-1]:
                continue
            else:
                count = 1
        return ans