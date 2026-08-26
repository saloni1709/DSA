class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: ints
        """
        
        f = {}
        for i in range(len(nums)):
            f[nums[i]] = f.get(nums[i], 0) + 1

            if f[nums[i]] > len(nums)//2:
                return nums[i]
        